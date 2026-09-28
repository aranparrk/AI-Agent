package 회원정보예제;

import java.util.Scanner;

public class MemberMain {
    public static void main(String[] args) {
        Member member = new Member();

        member.setName();
        member.setAge();
        member.setGender();
        member.setJob();
        member.getInfo();
    }
}
