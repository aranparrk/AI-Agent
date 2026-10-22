package com.human.mini_prj.controller;

import com.human.mini_prj.dto.CommentResDto;
import com.human.mini_prj.dto.CommentWriteReqDto;
import com.human.mini_prj.service.CommentService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Tag(name = "댓글 API", description = "댓글 조회, 작성, 수정, 삭제")
@Slf4j
@RestController
@RequestMapping("/comment")
@RequiredArgsConstructor
public class CommentController {
    private final CommentService commentService;

    // 댓글 조회
    @Operation(summary = "댓글 목록 조회", description = "게시글 ID로 해당 게시글의 댓글을 조회합니다.")
    @GetMapping("/list/{boardId}")
    public ResponseEntity<List<CommentResDto>> commentList(@PathVariable Long boardId) {
        return ResponseEntity.ok(commentService.getCommentListByBoard(boardId));
    }

    // 댓글 작성
    @Operation(summary = "댓글 작성", description = "새로운 댓글을 등록합니다.")
    @PostMapping("/write")
    public ResponseEntity<Boolean> writeComment(
            @RequestBody CommentWriteReqDto commentWriteReqDto) {

        return ResponseEntity.ok(
                commentService.createComment(commentWriteReqDto)
        );
    }

    // 댓글 수정
    @Operation(summary = "댓글 수정", description = "댓글 ID로 기존 댓글을 수정합니다.")
    @PutMapping("/update/{id}")
    public ResponseEntity<Boolean> updateComment(
            @PathVariable Long id,
            @RequestBody CommentWriteReqDto commentWriteReqDto) {

        return ResponseEntity.ok(
                commentService.updateComment(id, commentWriteReqDto)
        );
    }

    // 댓글 삭제
    @Operation(summary = "댓글 삭제", description = "댓글 ID로 해당 댓글을 삭제합니다.")
    @DeleteMapping("/delete/{id}")
    public ResponseEntity<Boolean> deleteComment(@PathVariable Long id) {
        return ResponseEntity.ok(
                commentService.deleteComment(id)
        );
    }
}