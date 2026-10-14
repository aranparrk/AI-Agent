package com.human.mini_prj.service;

import com.human.mini_prj.dto.CommentResDto;
import com.human.mini_prj.dto.CommentWriteReqDto;
import com.human.mini_prj.dto.PageResDto;
import com.human.mini_prj.entity.Board;
import com.human.mini_prj.entity.Comment;
import com.human.mini_prj.entity.Member;
import com.human.mini_prj.repository.BoardRepository;
import com.human.mini_prj.repository.CommentRepository;
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
@Transactional
@RequiredArgsConstructor
public class CommentService {
    private final CommentRepository commentRepository;
    private final BoardRepository boardRepository;
    private final MemberRepository memberRepository;

    // 댓글 조회
    @Transactional(readOnly = true)
    public List<CommentResDto> getCommentListByBoard(Long boardId) {
        List<Comment> commentList = commentRepository.findByBoard_IdOrderByRegDateAscCommentIdAsc(boardId);
        List<CommentResDto> commentResDtoList = new ArrayList<>();
        for (Comment comment : commentList) {
            commentResDtoList.add(toDto(comment));
        }

        return commentResDtoList;
    }

    // 댓글 작성
    public boolean createComment(CommentWriteReqDto dto) {
        try {
            Optional<Board> board = boardRepository.findById(dto.getBoardId());
            Optional<Member> member = memberRepository.findByEmail(dto.getEmail());
            if (board.isEmpty() || member.isEmpty()) {
                throw new IllegalArgumentException("회원이나 게시글이 없습니다");
            }
            Comment comment = new Comment();
            comment.setBoard(board.get());
            comment.setMember(member.get());
            comment.setContent(dto.getContent());
            commentRepository.save(comment);
            return true;
        } catch (Exception e) {
            log.error("댓글 작성을 실패하였습니다. {}", e.getMessage());
            return false;
        }
    }

    // 댓글 수정
    public boolean updateComment(Long id, CommentWriteReqDto dto) {
        try {
            Optional<Comment> comment = commentRepository.findById(id);

            if (comment.isEmpty()) {
                throw new IllegalArgumentException("댓글이 존재하지 않습니다.");
            }

            Comment findComment = comment.get();
            findComment.setContent(dto.getContent());

            return true;

        } catch (Exception e) {
            log.error("댓글 수정을 실패하였습니다.", e);
            return false;
        }
    }

    // 댓글 삭제
    public boolean deleteComment(Long id) {
        try {
            Optional<Comment> comment = commentRepository.findById(id);
            if  (comment.isEmpty()) {
                throw new IllegalArgumentException("댓글이 존재하지 않습니다.");
            }

            commentRepository.deleteById(id);

            return true;
        } catch (Exception e) {
            log.error("댓글 삭제를 실패하였습니다.", e);
            return false;
        }
    }

    // 내가 쓴 댓글 조회
    @Transactional(readOnly = true)
    public PageResDto<CommentResDto> getMyCommentPage(String email, int page, int size) {
        Optional<Member> member = memberRepository.findByEmail(email);

        if  (member.isEmpty()) {
            throw new IllegalArgumentException("회원이 존재하지 않습니다.");
        }

        Pageable pageable = PageRequest.of(page, size, Sort.by(Sort.Direction.DESC, "regDate"));

        Page<Comment> commentPage = commentRepository.findByMemberEmail(email, pageable);

        return new PageResDto<>(commentPage.map(this::toDto));
    }

    // Entity -> DTO
    private CommentResDto toDto(Comment comment) {
        CommentResDto dto = new CommentResDto();
        dto.setCommentId(comment.getCommentId());
        dto.setBoardId(comment.getBoard().getId());
        dto.setMemberId(comment.getMember().getId());
        dto.setContent(comment.getContent());
        dto.setRegDate(comment.getRegDate());
        return dto;
    }
}
