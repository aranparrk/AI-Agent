package 영화표예매하기;

import java.util.Scanner;

public class MovieMain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        MovieTicket mt = new MovieTicket(12000);

        while (true) {
            System.out.println("[1] 예매하기");
            System.out.println("[2] 취소하기");
            System.out.println("[3] 종료하기");

            try {
                int menuNum = Integer.parseInt(sc.nextLine());

                if (menuNum == 1) {
                    mt.printSeat();
                    System.out.println("===========================");
                    System.out.println("예매할 좌석을 선택하세요. (엔터: 메뉴)");

                    String seatNumStr = sc.nextLine();

                    if (seatNumStr.trim().isEmpty()) {
                        System.out.println("메뉴로 돌아갑니다.");
                        continue;
                    }

                    int seatNum = Integer.parseInt(seatNumStr);
                    mt.selectSeat(seatNum);

                } else if (menuNum == 2) {
                    mt.printSeat();
                    System.out.println("===========================");
                    System.out.println("취소할 좌석을 선택하세요. (엔터: 메뉴)");

                    String seatNumStr = sc.nextLine();

                    if (seatNumStr.trim().isEmpty()) {
                        System.out.println("메뉴로 돌아갑니다.");
                        continue;
                    }

                    int seatNum = Integer.parseInt(seatNumStr);
                    mt.cancelSeat(seatNum);

                } else if (menuNum == 3) {
                    System.out.println("총 판매 금액 : " + mt.totalAmount() + "원");
                    break;

                } else {
                    System.out.println("없는 메뉴 번호입니다.");
                }

            } catch (NumberFormatException e) {
                System.out.println("숫자를 입력해주세요.");
            }
        }
    }
}