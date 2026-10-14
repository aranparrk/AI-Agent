package com.human.mini_prj.controller;

import com.human.mini_prj.dto.*;
import com.human.mini_prj.service.BoardService;
import com.human.mini_prj.service.CommentService;
import com.human.mini_prj.service.MemberService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@RestController
@RequestMapping("/member")
@RequiredArgsConstructor
public class MemberController {
    private final MemberService memberService;
    private final BoardService boardService;
    private final CommentService commentService;

    // 회원 전체 조회
    @GetMapping("/list")
    public ResponseEntity<List<MemberResDto>> memberList() {
        return ResponseEntity.ok(memberService.getMemberList());
    }

    // 회원 상세 조회 : GET http://localhost:8111/member/{email}
    @GetMapping("/{email}")
    public ResponseEntity<MemberResDto> memberDetail(@PathVariable String email) {
        try {
            return ResponseEntity.ok(memberService.getMemberDetail(email));
        } catch (IllegalArgumentException e) {
            return ResponseEntity.notFound().build();  // 404
        }
    }

    // 회원 수정 : PUT http://localhost:8111/member/modify
    @PutMapping("/modify")
    public ResponseEntity<Boolean> memberModify(@RequestBody MemberUpdateReqDto dto) {
        return ResponseEntity.ok(memberService.updateMember(dto));
    }

    // 회원 삭제 : DELETE http://localhost:8111/member/{email}
    @DeleteMapping("/{email}")
    public ResponseEntity<Boolean> memberDelete(@PathVariable String email) {
        return ResponseEntity.ok(memberService.deleteMember(email));
    }

    // 회원 목록 페이지션 조회
    // GET http://localhost:8111/member/list/page?page=1&size=10
    @GetMapping("/list/page")
    public ResponseEntity<PageResDto<MemberResDto>> memberListPage(@RequestParam(defaultValue = "1") int page, @RequestParam(defaultValue = "10") int size) {
        return ResponseEntity.ok(memberService.getMemberPage(page, size));
    }

    // 내가 쓴 게시글 조회
    // GET http://localhost:8111/member/{email}/boards?page=0&size=10
    @GetMapping("/{email}/boards")
    public ResponseEntity<PageResDto<BoardResDto>> myBoardList(@PathVariable String email, @RequestParam(defaultValue = "1") int page, @RequestParam(defaultValue = "10") int size) {
        return ResponseEntity.ok(boardService.getMyBoardPage(email, page, size));
    }

    // 내가 쓴 댓글 조회
    // GET http://localhost:8111/member/{email}/comments?page=0&size=10
    @GetMapping("/{email}/comments")
    public ResponseEntity<PageResDto<CommentResDto>> myCommentList(@PathVariable String email, @RequestParam(defaultValue = "1") int page, @RequestParam(defaultValue = "10") int size) {
        return ResponseEntity.ok(commentService.getMyCommentPage(email, page, size));
    }
}