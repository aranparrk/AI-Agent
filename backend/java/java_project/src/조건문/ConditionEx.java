package 조건문;

// 조건문 : 주어진 조건식의 결과에 따라 별도의 명령을 수행하도록 제어하는 명령문
// if ~ else ~ if
// switch ~ case
// 3항 연산자

import java.util.Scanner;

public class ConditionEx {
    public static void main(String[] args) {
        // 나이를 입력 받아 19세까지는 미성년자 출력, 19세 초과하면 성인 출력
        // 3가지의 조건문을 사용해 출력 해보기
        Scanner sc = new Scanner(System.in); // 표준 입력으로 스캐너 객체 생성

        System.out.println("나이 : ");

        // 나이 입력 받기
        int age = sc.nextInt();

        // if문으로 참과 거짓 분기
        if (0 < age && age < 20) {
            System.out.println("미성년자");
        } else if (19 < age && age < 150) {
            System.out.println("성인");
        } else {
            System.out.println("잘못된 나이");
        }

        // 3항연산자를 사용해 출력하기
        System.out.println(
                age <= 0 || age >= 150
                        ? "잘못된 나이"
                        : age < 20
                        ? "미성년자"
                        : "성인"
        );

        // 숫자를 입력 받아 홀수 / 짝수 구분 해서 출력하기
        System.out.println("정수 : ");

        int num = sc.nextInt();

        if (num % 2 == 0) {
            System.out.println("짝수");
        } else {
            System.out.println("홀수");
        }

        System.out.println(num % 2 == 0 ? "짝수" : "홀수");

    }
}
