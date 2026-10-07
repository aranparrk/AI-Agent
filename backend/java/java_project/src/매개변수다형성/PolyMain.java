package 매개변수다형성;

// 오버라이딩 : 부모 클래스의 메서드를 자식 클래스에서 재정의하여 사용, 동적 다형성 또는 동적 바인딩이라고 함

import java.util.Scanner;

public class PolyMain {
    public static void main(String[] args) {
        Driver driver = new Driver("원이");
        Scanner sc = new Scanner(System.in);

        System.out.print("운전할 차량 선택 [1]스포츠카 [2]승용차 [3]트럭 : ");

        int menu =  sc.nextInt();

        switch (menu) {
            case 1:
                driver.drive(new SportsCar());
                break;
            case 2:
                driver.drive(new Sedan());
                break;
            case 3:
                driver.drive(new Truck());
                break;
            default:
                System.out.println("차량 선택이 잘못 되었습니다.");
        }
    }
}
