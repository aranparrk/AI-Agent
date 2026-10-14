package com.human.mini_prj.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;

@Getter
@Setter
@NoArgsConstructor
public class CommentResDto {
    private Long memberId;
    private Long boardId;
    private String content;
    private Long commentId;
    private LocalDateTime regDate;
}
