package com.human.mini_prj.service;

import com.human.mini_prj.dto.BoardLikeResDto;
import com.human.mini_prj.entity.Board;
import com.human.mini_prj.entity.BoardLike;
import com.human.mini_prj.entity.Member;
import com.human.mini_prj.repository.BoardLikeRepository;
import com.human.mini_prj.repository.BoardRepository;
import com.human.mini_prj.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

@Slf4j
@Service
@Transactional
@RequiredArgsConstructor
public class BoardLikeService {
    private final BoardLikeRepository boardLikeRepository;
    private final BoardRepository boardRepository;
    private final MemberRepository memberRepository;

    public BoardLikeResDto toggleLike(Long boardId, String email) {
        Optional<Board> board = boardRepository.findById(boardId);
        Optional<Member> member = memberRepository.findByEmail(email);
        boolean liked;

        if(board.isEmpty() || member.isEmpty()) {
            throw new IllegalArgumentException("존재하지 않는 회원이거나 존재하지 않는 게시글 입니다.");
        }

        Optional<BoardLike> boardLike = boardLikeRepository.findByBoardIdAndMemberEmail(boardId, email);

        if (boardLike.isPresent()) {
            boardLikeRepository.delete(boardLike.get());
            liked = false;
        } else {
            BoardLike newLike = new BoardLike();
            newLike.setBoard(board.get());
            newLike.setMember(member.get());

            boardLikeRepository.save(newLike);
            liked = true;
        }

        // 좋아요 등록 또는 삭제 후 전체 개수 조회
        long likeCount = boardLikeRepository.countByBoardId(boardId);

        BoardLikeResDto dto = new BoardLikeResDto();
        dto.setLiked(liked);
        dto.setLikeCount(likeCount);

        return dto;
    }
}
