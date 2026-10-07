package com.human.mini_prj.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

// 로그인 요청
@Setter
@Getter
@NoArgsConstructor
public class LoginReqDto {
    private String email;
    private String password;
}
