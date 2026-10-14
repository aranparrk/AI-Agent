package com.human.mini_prj.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "board")
@Getter
@Setter
@ToString
public class Board {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "board_id")
    private Long id; // PK는 자동 증가

    @Lob
    @Column(length = 10000)
    private String content; // 게시글 내용

    @Column(length = 100, nullable = false)
    private String title; // 게시글 제목

    private LocalDateTime regTime;
    @PrePersist
    public void prePersist() {
        this.regTime = LocalDateTime.now();
    }

    @ManyToOne(fetch = FetchType.LAZY) // 다대일 관계, 지연 전략
    @JoinColumn(name = "member_id") // 외래키
    private Member member; // 작성자 객체를 가져옴

    @OneToMany(mappedBy = "board", cascade = CascadeType.REMOVE)
    private List<Comment> comments = new ArrayList<>();
}
