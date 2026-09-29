package 영화표예매하기;

import java.util.Scanner;

public class MovieMain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // MovieTicket 클래스에 대한 ticket 참조 변수에 MovieTicket 객체 주소 대입
        MovieTicket ticket = new MovieTicket(12000);

        while (true) {
            System.out.println("[1] 예매하기");
            System.out.println("[2] 취소하기");
            System.out.println("[3] 종료하기");
            System.out.print("메뉴 선택 :");

            try {
                int menuNum = Integer.parseInt(sc.nextLine());

                switch (menuNum) {
                    case 1: {
                        ticket.printSeat();
                        System.out.println("===========================");
                        System.out.println("예매할 좌석을 선택하세요. (엔터: 메뉴)");

                        String seatNumStr = sc.nextLine();

                        if (seatNumStr.trim().isEmpty()) {
                            System.out.println("메뉴로 돌아갑니다.");
                            continue;
                        }

                        int seatNum = Integer.parseInt(seatNumStr);
                        ticket.selectSeat(seatNum);
                        break;
                    }

                    case 2: {
                        ticket.printSeat();
                        System.out.println("===========================");
                        System.out.println("취소할 좌석을 선택하세요. (엔터: 메뉴)");

                        String seatNumStr = sc.nextLine();

                        if (seatNumStr.trim().isEmpty()) {
                            System.out.println("메뉴로 돌아갑니다.");
                            continue;
                        }

                        int seatNum = Integer.parseInt(seatNumStr);
                        ticket.cancelSeat(seatNum);
                        break;
                    }

                    case 3:
                        System.out.println("총 판매 금액 : " + ticket.totalAmount() + "원");
                        return;

                    default:
                        System.out.println("없는 메뉴 번호입니다.");
                }

            } catch (NumberFormatException e) {
                System.out.println("숫자를 입력해주세요.");
            }
        }
    }
}