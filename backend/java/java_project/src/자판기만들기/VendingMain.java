package 자판기만들기;

import java.util.Scanner;

public class VendingMain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("================================");
        System.out.println("       🥤 자판기에 오신걸 환영합니다!");
        System.out.println("================================");
        System.out.println("1. 콜라      - 1,500원");
        System.out.println("2. 사이다    - 1,500원");
        System.out.println("3. 커피      - 1,000원");
        System.out.println("4. 생수      -   500원");
        System.out.println("================================");

        System.out.print("투입 금액 입력 : ");
        int money = sc.nextInt();

        System.out.print("메뉴 번호 입력 : ");
        int menu = sc.nextInt();

        String item = "";
        int price = 0;

        switch (menu) {
            case 1:
                item = "콜라";
                price = 1500;
                break;
            case 2:
                item = "사이다";
                price = 1500;
                break;
            case 3:
                item = "커피";
                price = 1000;
                break;
            case 4:
                item = "생수";
                price = 500;
                break;
            default:
                System.out.println("없는 메뉴 입니다.");
                sc.close();
                return;
        }

        System.out.println("================================");

        if (money < price) {
            System.out.println("❌ 잔액이 부족합니다.");
            System.out.println("투입 금액 : " + money + "원");
            System.out.println("필요 금액 : " + price + "원");
            System.out.println("부족 금액 : " + (price - money) + "원");
        } else {
            int change = money - price;
            System.out.println("✅ " + item + " 가 나왔습니다!");
            System.out.println("투입 금액 : " + money + "원");
            System.out.println("상품 금액 : " + price + "원");
            System.out.println("거스름돈  : " + change + "원");
        }

        System.out.println("================================");

        sc.close();

    }
}