package Math클래스;

// Math 클래스 : 수학에서 자주 사용하는 상수들과 함수를 미리 구현해 놓은 클래스
// - Math 클래스의 모든 메서드는 클래스 메서드(static method)이므로, 객체를 생성하지 않고도 바로 사용

import java.util.ArrayList;
import java.util.List;

public class MathMain {
    public static void main(String[] args) {
        // random 메서드 : 0.0 이상 1.0 미만의 범위에서 임의의 double형 값을 하나 생성하여 반환
        // 1 ~ 45 사이의 임의의 정수 만들기
        int val = (int)(Math.random() * 45 + 1); // 1 ~ 45 사이의 임의의 값

        // 1 ~ 100 사이의 중복되지 않는 값 10개 생성하기
        List<Integer> list = new ArrayList<>();

        while(list.size() < 10){
            int num =  (int)(Math.random() * 100 + 1);
            if (!list.contains(num)){ // 중복 확인
                list.add(num);
            }
        }

        // 중복 되지 않는 로또 번호 생성기 만들기
        // 1 ~ 45 사이의 중복되지 않는 임의의 값 6개
        List<Integer> lotto = new ArrayList<>();

        while(lotto.size() < 6){
            int num =  (int)(Math.random() * 45 + 1);
            if(!lotto.contains(num)){
                lotto.add(num);
            }
        }


        System.out.println(val);
        System.out.println(list);

        lotto.sort(null);
        System.out.println(lotto);

        System.out.println("=".repeat(30));
        System.out.println(Math.abs(10));               // 10
        System.out.println(Math.abs(-10));              // 10
        System.out.println(Math.abs(-3.14));            // 3.14

        // ceil() : 소수점이하가 있으면 무조건 올림
        System.out.println("=".repeat(30));
        System.out.println(Math.ceil(10.0));            // 10.0
        System.out.println(Math.ceil(10.1));            // 11.0
        System.out.println(Math.ceil(10.00000001));     // 11.0

        // floor() : 소수점 이하를 무조건 날림
        System.out.println("=".repeat(30));
        System.out.println(Math.floor(10.0));           // 10.0
        System.out.println(Math.floor(10.9));           // 10.0
        System.out.println(Math.floor(10.0000001));     // 10.0

        // round() : 반올림
        System.out.println("=".repeat(30));
        System.out.println(Math.round(10.0));           // 10
        System.out.println(Math.round(10.4999));        // 10
        System.out.println(Math.round(10.5));           // 11

        // max()와 min()
        int x = 10;
        int y = 20;
        System.out.println("=".repeat(30));
        System.out.println(Math.max(x, y));             // 20
        System.out.println(Math.min(x, y));             // 10

    }
}
