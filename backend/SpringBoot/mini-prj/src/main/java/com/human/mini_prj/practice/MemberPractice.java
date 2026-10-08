package com.human.mini_prj.practice;

import com.human.mini_prj.entity.Member;
import com.human.mini_prj.repository.MemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
public class MemberPractice {

    private final MemberRepository memberRepository;

    // 회원 전체 조회
    public List<Member> getAllMember() {
        return memberRepository.findAll();
    }

    // 회원 상세 조회
    public Optional<Member> getMemberById(Long id) {
        return memberRepository.findById(id);
    }


}