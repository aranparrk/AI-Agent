
package com.human.mini_prj.controller;

import com.human.mini_prj.dto.LoginReqDto;
import com.human.mini_prj.dto.SignUpReqDto;
import com.human.mini_prj.service.AuthService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@Tag(name = "인증 API", description = "이메일 중복 확인, 회원가입 및 로그인")
@Slf4j
@RestController                 // Restfull API, 직렬화 / 역직렬화 기능 제공
@RequestMapping("/auth")        // http://localhost:8111/auth/ 접근경로
@RequiredArgsConstructor
@CrossOrigin(origins = {"http://localhost:3000", "http://localhost:3001"})
public class AuthController {
    private final AuthService authService;  // 생성자를 통한 의존성 주입

    // 회원 가입 여부 확인
    @Operation(summary = "이메일 중복 확인", description = "입력한 이메일이 이미 가입되어 있는지 확인합니다.")
    @GetMapping("/exists/{email}")
    public boolean existsEmail(@PathVariable String email) {
        return authService.isDuplicatedEmail(email);
    }

    // 회원 가입
    @Operation(summary = "회원가입", description = "회원 정보를 전달받아 새로운 회원을 등록합니다.")
    @PostMapping("/signup")
    public ResponseEntity<Boolean> signUp(@RequestBody SignUpReqDto dto) {
        return ResponseEntity.ok(authService.singUp(dto));
    }

    // 로그인
    @Operation(summary = "로그인", description = "이메일과 비밀번호를 이용하여 로그인을 검증합니다.")
    @PostMapping("/login")
    public ResponseEntity<Boolean> login(@RequestBody LoginReqDto dto) {
        return ResponseEntity.ok(authService.login(dto.getEmail(), dto.getPwd()));
    }
}
