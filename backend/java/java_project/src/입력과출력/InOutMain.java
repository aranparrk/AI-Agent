package 입력과출력;

public class InOutMain { // 자바 클래스 이름은 대문자로 시작해야 함
    public static void main(String[] args) {
        // System.in : 표준 입력 스트림
        // System.out : 표준 출력 스트림
        // System.err : 표준 오류 스트림, 거의 사용 되지 않음

        // 이름, 주소, 성별, 국어, 영어, 수학 변수를 만들고 값을 대입
        // 총점과 평균 구하기
        // 이름, 주소, 성별, 총점, 평균을 println()과 printf()로 출력
        String name = "박아란";
        String addr = "경기도 수원";
        char gender = 'F';
        int kor = 80;
        int math = 33;
        int eng = 77;
        int total = kor + math + eng;
        double avg = (double)total / 3;
        // println() 자바의 오버로딩 문법을 사용, 데이터 타입을 자동으로 찾아줌
        System.out.println("====== Java Style output ======");
        System.out.println("이름 : " + name);
        System.out.println("주소 : " + addr);
        System.out.println("성별 : " + gender);
        System.out.println("총점 : " + total);
        System.out.println("평균 : " + avg);
        // printf() 서식 지정자를 사용해서 출력 하는 방식
        System.out.println("====== printf Style ======");
        System.out.printf("이름 : " + "%s%n", name);
        System.out.printf("주소 : " + "%s%n", addr);
        System.out.printf("성별 : " + "%c%n", gender);
        System.out.printf("총점 : " + "%d%n", total);
        System.out.printf("평균 : " + "%.2f%n", avg);
        System.out.println();

        // 실습문제 1
        System.out.println("================================");
        System.out.println("       나를 소개합니다!");
        System.out.println("================================");
        System.out.println("이름\t : 박아란");
        System.out.println("나이\t : 33세");
        System.out.println("취미\t : 코딩, 독서, 운동");
        System.out.println("한마디 : \"안녕하세요, 잘 부탁드립니다!\"");
        System.out.println("================================");
        System.out.println();

        // 실습문제 2
        System.out.println("================================");
        System.out.println("     JAVA CAFE 영수증");
        System.out.println("================================");
        System.out.printf("%-12s %3d잔 %,7d원%n", "아메리카노", 2, 9000);
        System.out.printf("%-12s %3d잔 %,7d원%n", "카페라떼", 1, 5500);
        System.out.printf("%-12s %3d조각 %,7d원%n", "치즈케이크", 1, 6800);
        System.out.println("------------------------------");
        System.out.printf("%-12s %,14d원%n", "합  계", 21300);
        System.out.println("================================");
        System.out.println("감사합니다. 또 방문해주세요!");
        System.out.println();

        // 실습문제 3
        System.out.println("─────────────────────");
        System.out.println("     구구단  3단       ");
        System.out.println("─────────────────────");
        System.out.println("3 X 1 = 3");
        System.out.println("3 X 2 = 6");
        System.out.println("3 X 3 = 9");
        System.out.println("3 X 4 = 12");
        System.out.println("3 X 5 = 15");
        System.out.println("3 X 6 = 18");
        System.out.println("3 X 7 = 21");
        System.out.println("3 X 8 = 24");
        System.out.println("3 X 9 = 27");
    }
}
