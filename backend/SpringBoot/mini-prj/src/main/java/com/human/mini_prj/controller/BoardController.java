package com.human.mini_prj.controller;

import com.human.mini_prj.dto.BoardResDto;
import com.human.mini_prj.dto.BoardWriteReqDto;
import com.human.mini_prj.service.BoardService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j
@RestController
@RequestMapping("/board")
@RequiredArgsConstructor
public class BoardController {

    private final BoardService boardService;

    // 게시글 전체 조회
    @GetMapping("/list")
    public ResponseEntity<List<BoardResDto>> boardList() {
        return ResponseEntity.ok(boardService.getBoardList());
    }

    // 게시글 상세 조회
    @GetMapping("/{id}")
    public ResponseEntity<BoardResDto> boardDetail(@PathVariable Long id) {
        try {
            return ResponseEntity.ok(boardService.getBoardDetail(id));
        } catch (IllegalArgumentException e) {
            return ResponseEntity.notFound().build(); // 404
        }
    }

    // 게시글 작성
    @PostMapping("/write")
    public ResponseEntity<Boolean> boardWrite(
            @RequestBody BoardWriteReqDto boardWriteReqDto) {

        try {
            return ResponseEntity.ok(
                    boardService.writeBoard(boardWriteReqDto)
            );
        } catch (Exception e) {
            log.error("게시글 작성 실패", e);
            return ResponseEntity.internalServerError().body(false);
        }
    }

    @PutMapping("/{id}")
    public ResponseEntity<Boolean> boardUpdate(
            @PathVariable Long id,
            @RequestBody BoardWriteReqDto boardWriteReqDto) {

        try {
            return ResponseEntity.ok(
                    boardService.updateBoard(id, boardWriteReqDto)
            );
        } catch (Exception e) {
            log.error("게시글 수정 실패", e);
            return ResponseEntity.internalServerError().body(false);
        }
    }

    // 게시글 삭제
    @DeleteMapping("/{id}")
    public ResponseEntity<Boolean> boardDelete(@PathVariable Long id) {
        try {
            return ResponseEntity.ok(boardService.deleteBoard(id));

        } catch (Exception e) {
            log.error("게시글 삭제 실패", e);
            return ResponseEntity.internalServerError().body(false);

        }
    }
}