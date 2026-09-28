package 스위치문;

// switch문도 if문과 마찬가지로 조건 제어문
// 변수의 값에 따라 분기 함 (조건식이 올 수 없음)

import java.util.Scanner;

public class SwitchMain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("계산식 입력 : ");
        int x =  sc.nextInt();
        char op = sc.next().charAt(0);
        int y = sc.nextInt();

        switch (op) {
            case '+' :
                System.out.println(x + y);
                break;
            case '-' :
                System.out.println(x - y);
                break;
            case '*' :
                System.out.println(x * y);
                break;
            case '/' :
                System.out.println((double)x / y);
                break;
            default:
                System.out.println("계산식을 잘못 입력 하셨습니다.");
        }
    }
}
