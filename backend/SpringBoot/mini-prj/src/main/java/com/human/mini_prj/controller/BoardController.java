package com.human.mini_prj.controller;

import com.human.mini_prj.dto.BoardResDto;
import com.human.mini_prj.dto.BoardWriteReqDto;
import com.human.mini_prj.dto.PageResDto;
import com.human.mini_prj.service.BoardService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Slf4j                       // log 메시지 작성 하는 용도
@RestController              // Restfull API를 지원하는 컨트롤러(직렬화 / 역직렬화) 기능을 가지고 있음
@RequestMapping("/board")    // http:/localhost:8111/board/
@RequiredArgsConstructor     // 생성자를 통한 의존성 주입을 자동 생성
public class BoardController {

    private final BoardService boardService; // 의존성 주입

    // 게시글 전체 조회
    @GetMapping("/list")
    // 객체를 반환
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

    // 보드 목록 페이지션 조회
    // GET http://localhost:8111/board/list/page?page=1&size=10
    @GetMapping("/list/page")
    public ResponseEntity<PageResDto<BoardResDto>> boardListPage(@RequestParam(defaultValue = "1") int page, @RequestParam(defaultValue = "10") int size) {
        return ResponseEntity.ok(boardService.getBoardPage(page, size));
    }
}