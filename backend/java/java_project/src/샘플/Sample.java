package 샘플;

// 단일행 주석
/*
*   저자 : 박아란
*   일자 : 2026. 09. 28
*   목적 : 샘플 프로그램
* */

public class Sample { // 자바는 클래스 기반의 언어이므로 반드시 클래스 필요
    public static void main(String[] args) {
        // 프로그램의 시작 메서드
        System.out.println("안녕하세요. 자바 프로그램 입니다."); // 자바는 반드시 ;(세미콜론)으로 끝나야 함

        // 자바의 기본 출력 : print(), println(), printf()
        System.out.print(7); // print() 메소드는 줄 바꿈을 하지 않음
        System.out.println(3); // 정수 출력
        System.out.println(3.14); // 실수 출력
        System.out.println("자바!"); // 문자열 출력
        System.out.println("문자열끼리의 " + "연결도 가능합니다.");
        System.out.println("숫자" + 3 + "과 문자열의 연결도 가능합니다.");
        System.out.printf("%d\n", 3); // 서식 지정자 사용

    }
}
