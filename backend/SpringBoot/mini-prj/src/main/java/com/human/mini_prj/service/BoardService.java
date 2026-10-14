package com.human.mini_prj.service;

import com.human.mini_prj.dto.BoardResDto;
import com.human.mini_prj.dto.BoardWriteReqDto;
import com.human.mini_prj.dto.PageResDto;
import com.human.mini_prj.entity.Board;
import com.human.mini_prj.entity.Member;
import com.human.mini_prj.repository.BoardRepository;
import com.human.mini_prj.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Slf4j
@Service
@RequiredArgsConstructor
@Transactional
public class BoardService {
    private final BoardRepository boardRepository;
    private final MemberRepository memberRepository;

    // 게시글 전체 조회
    @Transactional(readOnly = true)
    public List<BoardResDto> getBoardList() {
        List<Board> boardList = boardRepository.findAllByOrderByRegDateDesc();
        List<BoardResDto> boardResDtoList = new ArrayList<>();
        for (Board board : boardList) {
            boardResDtoList.add(toDto(board));
        }
        return boardResDtoList;
    }

    // 게시글 상세 조회
    public BoardResDto getBoardDetail(Long id) {
        Optional<Board> board = boardRepository.findById(id);
        if (board.isEmpty()) {
            throw new IllegalArgumentException("해당 게시글이 존재하지 않습니다.");
        }
        Board viewBoard = board.get();

        viewBoard.setViewCount(viewBoard.getViewCount() + 1);

        return toDto(viewBoard);
    }

    // 게시글 작성
    public boolean writeBoard(BoardWriteReqDto dto) {
        try {
            // 작성자 조회
            Optional <Member> member = memberRepository.findByEmail(dto.getEmail());
            if (member.isEmpty()) {
                throw new IllegalArgumentException("해당 회원이 존재하지 않습니다.");
            }
            Board board = new Board();
            board.setMember(member.get());
            board.setTitle(dto.getTitle());
            board.setContent(dto.getContent());
            boardRepository.save(board); // INSERT와 동일
            return true;
        } catch (Exception e) {
            log.error("게시글 작성 시 오류 발생 : {}",  e.getMessage());
            return false;
        }
    }

    // 게시글 수정
    public boolean updateBoard(Long id, BoardWriteReqDto dto) {
        try {
            Optional<Board> board = boardRepository.findById(id);
            if (board.isEmpty()) {
                throw new IllegalArgumentException("게시글이 존재하지 않습니다.");
            }
            Board findBoard = board.get();

            findBoard.setTitle(dto.getTitle());
            findBoard.setContent(dto.getContent());
            boardRepository.save(findBoard);

            return true;
        } catch (Exception e) {
            log.error("게시글 수정 시 오류 발생 {}", e.getMessage());
            return false;
        }

    }

    // 게시글 삭제
    public boolean deleteBoard(Long id) {
        try{
            Optional<Board> board = boardRepository.findById(id);
            if(board.isEmpty()){
                throw new IllegalArgumentException("게시글이 존재하지 않습니다.");
            }

            boardRepository.delete(board.get());

            return true;
        }catch (Exception e){
            log.error("게시글 삭제 시 오류 발생 {}", e.getMessage());
            return false;
        }
    }

    // 게시글 목록 페이지네이션 조회 (최신순)
    public PageResDto<BoardResDto> getBoardPage(int page, int size) {
        Pageable pageable = PageRequest.of(page, size, Sort.by(Sort.Direction.DESC, "regDate"));
        Page<Board> boardPage = boardRepository.findAll(pageable);
        Page<BoardResDto> boardResDtoPage = boardPage.map(this::toDto);
        return new PageResDto<>(boardResDtoPage);
    }

    // 게시글 검색 & 페이징
    @Transactional(readOnly = true)
    public PageResDto<BoardResDto> searchBoard(
            int page, int size, String keyword, String type) {

        Pageable pageable = PageRequest.of(
                page, size, Sort.by(Sort.Direction.DESC, "regDate")
        );

        Page<Board> boardPage;

        if ("title".equals(type)) {
            boardPage = boardRepository.findByTitleContaining(keyword, pageable);
        } else if ("content".equals(type)) {
            boardPage = boardRepository.findByContentContaining(keyword, pageable);
        } else if ("writer".equals(type)) {
            boardPage = boardRepository.findByMemberNameContaining(keyword, pageable);
        } else {
            boardPage = boardRepository.findByTitleContainingOrContentContaining(keyword, keyword, pageable);
        }

        Page<BoardResDto> boardResDtoPage = boardPage.map(this::toDto);
        return new PageResDto<>(boardResDtoPage);
    }

    // Entity -> Dto
    private BoardResDto toDto(Board board) {
        BoardResDto dto = new BoardResDto();
        dto.setId(board.getId());
        dto.setTitle(board.getTitle());
        dto.setContent(board.getContent());
        dto.setEmail(board.getMember().getEmail());
        dto.setName(board.getMember().getName());
        dto.setRegDate(board.getRegDate());
        dto.setViewCount(board.getViewCount());
        return dto;
    }
}
