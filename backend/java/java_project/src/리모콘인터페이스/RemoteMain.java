package 리모콘인터페이스;

import java.util.Scanner;

public class RemoteMain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        RemoteControl remote = null;

        while (true) {
            System.out.print("제품을 선택 [1]PlayStation [2]TV [3]Audio (엔터 > 종료) : ");

            String str = sc.nextLine();

            if (str.trim().isEmpty()) {
                System.out.println("종료합니다.");
                break;
            }

            try{
                int menu_num = Integer.parseInt(str);

                switch (menu_num) {
                    case 1:
                        remote = new PlayStation();
                        remote.turnOn();
                        remote.setVolume(110);
                        break;
                    case 2:
                        remote = new Television();
                        remote.turnOn();
                        remote.setVolume(90);
                        break;
                    case 3:
                        remote = new Audio();
                        remote.turnOn();
                        remote.setVolume(100);
                        break;
                    default:
                        System.out.println("잘못 입력하셨습니다.");
                        continue;
                }


            }catch (NumberFormatException e){
                System.out.println("숫자를 입력하세요.");
            }
        }



    }
}
