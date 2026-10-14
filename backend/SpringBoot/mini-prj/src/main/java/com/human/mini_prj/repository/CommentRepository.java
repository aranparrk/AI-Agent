package com.human.mini_prj.repository;

import com.human.mini_prj.entity.Comment;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CommentRepository extends JpaRepository<Comment, Long> {
    List<Comment> findByBoard_IdOrderByRegDateAscCommentIdAsc(Long boardId);

    Page<Comment> findByMemberEmail(String memberEmail, Pageable pageable);

    long countByBoardId(Long boardId);

    void deleteByBoardId(Long boardId);
}
