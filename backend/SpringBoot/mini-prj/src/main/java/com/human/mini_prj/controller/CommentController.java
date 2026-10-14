package com.human.mini_prj.controller;

import com.human.mini_prj.dto.CommentResDto;
import com.human.mini_prj.dto.CommentWriteReqDto;
import com.human.mini_prj.service.CommentService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@RestController
@RequestMapping("/comment")
@RequiredArgsConstructor
public class CommentController {
    private final CommentService commentService;

    // 댓글 조회
    @GetMapping("/list/{boardId}")
    public ResponseEntity<List<CommentResDto>> commentList(@PathVariable Long boardId) {
        return ResponseEntity.ok(commentService.getCommentListByBoard(boardId));
    }

    // 댓글 작성
    @PostMapping("/write")
    public ResponseEntity<Boolean> writeComment(
            @RequestBody CommentWriteReqDto commentWriteReqDto) {

        return ResponseEntity.ok(
                commentService.createComment(commentWriteReqDto)
        );
    }

    // 댓글 수정
    @PutMapping("/update/{id}")
    public ResponseEntity<Boolean> updateComment(
            @PathVariable Long id,
            @RequestBody CommentWriteReqDto commentWriteReqDto) {

        return ResponseEntity.ok(
                commentService.updateComment(id, commentWriteReqDto)
        );
    }

    // 댓글 삭제
    @DeleteMapping("/delete/{id}")
    public ResponseEntity<Boolean> deleteComment(@PathVariable Long id) {
        return ResponseEntity.ok(
                commentService.deleteComment(id));
    }
}
