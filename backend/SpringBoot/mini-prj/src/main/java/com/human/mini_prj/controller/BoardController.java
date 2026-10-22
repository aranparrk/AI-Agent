
package com.human.mini_prj.controller;

import com.human.mini_prj.dto.*;
import com.human.mini_prj.service.BoardLikeService;
import com.human.mini_prj.service.BoardService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Tag(name = "게시판 API", description = "게시글 조회, 작성, 수정, 삭제, 검색 및 좋아요")
@Slf4j                       // log 메시지 작성 하는 용도
@RestController              // Restfull API를 지원하는 컨트롤러(직렬화 / 역직렬화) 기능을 가지고 있음
@RequestMapping("/board")    // http://localhost:8111/board/
@RequiredArgsConstructor     // 생성자를 통한 의존성 주입을 자동 생성
public class BoardController {

    private final BoardService boardService; // 의존성 주입
    private final BoardLikeService boardLikeService;

    // 게시글 전체 조회
    @Operation(summary = "게시글 전체 조회", description = "등록된 모든 게시글을 조회합니다.")
    @GetMapping("/list")
    // 객체를 반환
    public ResponseEntity<List<BoardResDto>> boardList() {
        return ResponseEntity.ok(boardService.getBoardList());
    }

    // 게시글 상세 조회
    @Operation(summary = "게시글 상세 조회", description = "게시글 ID로 상세 정보를 조회하고 조회수를 증가시킵니다.")
    @GetMapping("/{id}")
    public ResponseEntity<BoardResDto> boardDetail(@PathVariable Long id) {
        try {
            return ResponseEntity.ok(boardService.getBoardDetail(id));
        } catch (IllegalArgumentException e) {
            return ResponseEntity.notFound().build(); // 404
        }
    }

    // 게시글 작성
    @Operation(summary = "게시글 작성", description = "새로운 게시글을 등록합니다.")
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

    @Operation(summary = "게시글 수정", description = "게시글 ID로 기존 게시글을 수정합니다.")
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
    @Operation(summary = "게시글 삭제", description = "게시글 ID로 해당 게시글을 삭제합니다.")
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
    @Operation(summary = "게시글 페이징 조회", description = "페이지 번호와 페이지 크기를 지정하여 게시글 목록을 조회합니다.")
    @GetMapping("/list/page")
    public ResponseEntity<PageResDto<BoardResDto>> boardListPage(@RequestParam(defaultValue = "1") int page, @RequestParam(defaultValue = "10") int size) {
        return ResponseEntity.ok(boardService.getBoardPage(page, size));
    }

    // 게시판 검색 페이징
    // GET http://localhost:8111/board/search?keyword=스프링&page=0&size=10
    @Operation(summary = "게시글 검색", description = "검색어와 검색 유형을 이용하여 게시글을 검색하고 페이징 처리합니다.")
    @GetMapping("/search")
    public ResponseEntity<PageResDto<BoardResDto>> boardSearch(@RequestParam(defaultValue = "1") int page, @RequestParam(defaultValue = "10") int size, @RequestParam String keyword, @RequestParam(required = false) String type) {
        return ResponseEntity.ok(boardService.searchBoard(page, size, keyword, type));
    }

    // 좋아요
    // POST http://localhost:8111/board/{id}/like
    @Operation(summary = "게시글 좋아요", description = "사용자 이메일을 이용하여 게시글의 좋아요 상태를 토글합니다.")
    @PostMapping("/{id}/like")
    public ResponseEntity<BoardLikeResDto> boardLike(@PathVariable Long id, @RequestBody BoardLikeReqDto dto) {
        return ResponseEntity.ok(boardLikeService.toggleLike(id, dto.getEmail()));
    }
}
