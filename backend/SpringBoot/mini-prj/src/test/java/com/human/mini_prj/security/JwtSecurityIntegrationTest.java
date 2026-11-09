package com.human.mini_prj.security;

import com.human.mini_prj.constant.Authority;
import com.human.mini_prj.repository.*;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.io.Encoders;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.webmvc.test.autoconfigure.AutoConfigureMockMvc;
import org.springframework.http.MediaType;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.transaction.annotation.Transactional;
import tools.jackson.databind.ObjectMapper;

import static org.junit.jupiter.api.Assertions.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
@ActiveProfiles("test")
@Transactional
class JwtSecurityIntegrationTest {
    @Autowired MockMvc mvc;
    @Autowired ObjectMapper mapper;
    @Autowired MemberRepository members;
    @Autowired BoardRepository boards;
    @Autowired CommentRepository comments;
    @Autowired BoardLikeRepository likes;
    @Autowired PasswordEncoder encoder;
    @Autowired TokenProvider tokens;

    private String signupAndLogin(String email) throws Exception {
        mvc.perform(post("/auth/signup").contentType(MediaType.APPLICATION_JSON)
                .content("{\"email\":\"" + email + "\",\"pwd\":\"password\",\"name\":\"tester\"}"))
                .andExpect(status().isOk()).andExpect(content().string("true"));
        var member = members.findByEmail(email).orElseThrow();
        assertNotEquals("password", member.getPwd());
        assertTrue(encoder.matches("password", member.getPwd()));
        assertEquals(Authority.ROLE_USER, member.getAuthority());

        var response = mvc.perform(post("/auth/login").contentType(MediaType.APPLICATION_JSON)
                .content("{\"email\":\"" + email + "\",\"pwd\":\"password\"}"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.grantType").value("Bearer"))
                .andExpect(jsonPath("$.accessTokenExpriesIn").isNumber())
                .andReturn().getResponse().getContentAsString();
        return mapper.readTree(response).get("accessToken").asString();
    }

    @Test
    void signupLoginAndStatelessAuthentication() throws Exception {
        String token = signupAndLogin("jwt@example.com");
        assertEquals("jwt@example.com", tokens.getAuthentication(token).getName());
        assertTrue(tokens.getAuthentication(token).getAuthorities().stream()
                .anyMatch(a -> a.getAuthority().equals("ROLE_USER")));
        mvc.perform(get("/auth/exists/jwt@example.com"))
                .andExpect(status().isOk()).andExpect(content().string("true"));
        mvc.perform(get("/member/list")).andExpect(status().isUnauthorized());
        var result = mvc.perform(get("/member/list").header("Authorization", "Bearer " + token))
                .andExpect(status().isOk()).andReturn();
        assertNull(result.getRequest().getSession(false));
        mvc.perform(get("/member/list")).andExpect(status().isUnauthorized());
        mvc.perform(post("/auth/login").contentType(MediaType.APPLICATION_JSON)
                .content("{\"email\":\"jwt@example.com\",\"pwd\":\"wrong\"}"))
                .andExpect(status().isUnauthorized())
                .andExpect(jsonPath("$.code").value("LOGIN_FAILED"));
        mvc.perform(post("/auth/login").contentType(MediaType.APPLICATION_JSON)
                .content("{\"email\":\"missing@example.com\",\"pwd\":\"wrong\"}"))
                .andExpect(status().isUnauthorized())
                .andExpect(jsonPath("$.code").value("LOGIN_FAILED"));
    }

    @Test
    void memberChangesUseAuthenticatedIdentity() throws Exception {
        String owner = signupAndLogin("member-owner@example.com");
        String stranger = signupAndLogin("member-stranger@example.com");
        mvc.perform(put("/member/modify").header("Authorization", "Bearer " + owner)
                .contentType(MediaType.APPLICATION_JSON)
                .content("{\"name\":\"updated\",\"image\":\"image.png\"}"))
                .andExpect(status().isOk()).andExpect(content().string("true"));
        assertEquals("updated", members.findByEmail("member-owner@example.com").orElseThrow().getName());
        assertEquals("tester", members.findByEmail("member-stranger@example.com").orElseThrow().getName());
        mvc.perform(delete("/member/member-owner@example.com").header("Authorization", "Bearer " + stranger))
                .andExpect(status().isOk()).andExpect(content().string("false"));
        assertTrue(members.existsByEmail("member-owner@example.com"));
        mvc.perform(delete("/member/member-owner@example.com").header("Authorization", "Bearer " + owner))
                .andExpect(status().isOk()).andExpect(content().string("true"));
        members.flush();
        assertFalse(members.existsByEmail("member-owner@example.com"));
    }

    @Test
    void publicEndpointsAndInvalidTokens() throws Exception {
        mvc.perform(get("/board/list")).andExpect(status().isOk());
        mvc.perform(get("/comment/list/1")).andExpect(status().isOk());
        mvc.perform(get("/v3/api-docs")).andExpect(status().isOk());
        mvc.perform(post("/board/write").contentType(MediaType.APPLICATION_JSON).content("{}"))
                .andExpect(status().isUnauthorized());
        String secret = Encoders.BASE64.encode(Jwts.SIG.HS512.key().build().getEncoded());
        var other = new TokenProvider(secret, 3600000);
        var expired = new TokenProvider(secret, -60000);
        for (String token : new String[]{"broken", other.createToken("x@example.com", Authority.ROLE_USER).accessToken(),
                expired.createToken("x@example.com", Authority.ROLE_USER).accessToken()}) {
            mvc.perform(get("/member/list").header("Authorization", "Bearer " + token))
                    .andExpect(status().isUnauthorized());
        }
        mvc.perform(options("/board/write").header("Origin", "http://localhost:3001")
                .header("Access-Control-Request-Method", "POST")
                .header("Access-Control-Request-Headers", "Authorization"))
                .andExpect(status().isOk())
                .andExpect(header().string("Access-Control-Allow-Origin", "http://localhost:3001"));
    }

    @Test
    void boardCommentAndLikeKeepExistingBehaviorAndCheckOwnership() throws Exception {
        String owner = signupAndLogin("owner@example.com");
        String stranger = signupAndLogin("stranger@example.com");
        mvc.perform(post("/board/write").header("Authorization", "Bearer " + owner)
                .contentType(MediaType.APPLICATION_JSON).content("{\"title\":\"jwt title\",\"content\":\"body\"}"))
                .andExpect(status().isOk()).andExpect(content().string("true"));
        long id = boards.findAll().getFirst().getId();
        mvc.perform(post("/comment/write").header("Authorization", "Bearer " + owner)
                .contentType(MediaType.APPLICATION_JSON).content("{\"boardId\":" + id + ",\"content\":\"comment\"}"))
                .andExpect(status().isOk()).andExpect(content().string("true"));
        long commentId = comments.findAll().getFirst().getCommentId();
        mvc.perform(put("/comment/" + commentId).header("Authorization", "Bearer " + stranger)
                .contentType(MediaType.APPLICATION_JSON).content("{\"content\":\"changed\"}"))
                .andExpect(status().isOk()).andExpect(content().string("false"));
        mvc.perform(delete("/comment/" + commentId).header("Authorization", "Bearer " + stranger))
                .andExpect(status().isOk()).andExpect(content().string("false"));
        mvc.perform(put("/board/" + id).header("Authorization", "Bearer " + stranger)
                .contentType(MediaType.APPLICATION_JSON).content("{\"title\":\"changed\",\"content\":\"changed\"}"))
                .andExpect(status().isOk()).andExpect(content().string("false"));
        mvc.perform(delete("/board/" + id).header("Authorization", "Bearer " + stranger))
                .andExpect(status().isOk()).andExpect(content().string("false"));
        mvc.perform(post("/board/" + id + "/like").header("Authorization", "Bearer " + stranger)
                .contentType(MediaType.APPLICATION_JSON).content("{\"email\":\"owner@example.com\"}"))
                .andExpect(status().isForbidden())
                .andExpect(jsonPath("$.code").value("FORBIDDEN"));
        assertEquals(0, likes.countByBoardId(id));
        mvc.perform(post("/board/" + id + "/like").header("Authorization", "Bearer " + owner)
                .contentType(MediaType.APPLICATION_JSON).content("{\"email\":\"owner@example.com\"}"))
                .andExpect(status().isOk()).andExpect(jsonPath("$.liked").value(true));
        mvc.perform(get("/board/" + id))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.viewCount").value(1))
                .andExpect(jsonPath("$.likeCount").value(1))
                .andExpect(jsonPath("$.commentCount").value(1));
        for (String type : new String[]{"title", "content", "writer", ""}) {
            mvc.perform(get("/board/search").param("keyword", "").param("page", "0").param("type", type))
                    .andExpect(status().isOk()).andExpect(jsonPath("$.totalElements").value(1));
        }
        mvc.perform(get("/member/owner@example.com/boards").param("page", "0")
                .header("Authorization", "Bearer " + owner))
                .andExpect(status().isOk()).andExpect(jsonPath("$.totalElements").value(1));
        mvc.perform(get("/member/owner@example.com/comments").param("page", "0")
                .header("Authorization", "Bearer " + owner))
                .andExpect(status().isOk()).andExpect(jsonPath("$.totalElements").value(1));
        mvc.perform(delete("/board/" + id).header("Authorization", "Bearer " + owner))
                .andExpect(status().isOk()).andExpect(content().string("true"));
        boards.flush();
        assertFalse(boards.existsById(id));
        assertEquals(0, comments.countByBoardId(id));
        assertEquals(0, likes.countByBoardId(id));
    }
}
