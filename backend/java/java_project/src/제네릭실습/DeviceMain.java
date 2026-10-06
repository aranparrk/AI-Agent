package 제네릭실습;

import java.util.Scanner;

public class DeviceMain {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(true){
            System.out.print("기기 선택 : [1]프린터 [2]모니터 [3]키보드 : ");
            String str = sc.nextLine();

            try{
                int menu_num =  Integer.parseInt(str);
                switch(menu_num){
                    case 1:
                        DeviceController<Printer> print = new DeviceController<>();
                        Printer printDevice = new Printer();

                        print.setDevice(printDevice);

                        print.powerOn();
                        print.powerOff();
                        break;
                    case 2:
                        DeviceController<Monitor> monitor = new DeviceController<>();

                        Monitor monitorDevice = new Monitor();

                        monitor.setDevice(monitorDevice);

                        monitor.powerOn();
                        monitor.powerOff();
                        break;
                    case 3:
                        DeviceController<KeyBoard> keyboard = new DeviceController<>();

                        KeyBoard keyBoardDevice = new KeyBoard();

                        keyboard.setDevice(keyBoardDevice);
                        keyboard.powerOn();
                        keyboard.powerOff();
                        break;
                    default:
                        System.out.println("없는 메뉴 입니다.");
                }

            }catch (NumberFormatException e){
                System.out.println("숫자를 입력해주세요.");
            }
        }
    }
}
