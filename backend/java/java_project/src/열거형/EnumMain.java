package 열거형;

// Enum 클래스 : 열거 타입(Enum Type)은 한정된 상수 집합을 정의할 수 있는 참조 타입

// 이름
// 개발 타입 : 모바일, 프론트, 백엔드, 데이터베이스
// 경력 : 신입과 경력
// 성별 : 남성, 여성
// 주소

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class EnumMain {
    static Scanner sc = new Scanner(System.in);
    static List<Developer> devList = new ArrayList<>();
    public static void main(String[] args) {
//        Developer developer = new Developer("장원영", DevType.FRONTEND, Career.JUNIOR, Gender.FEMALE, "경기도 수원시");

        while (true) {
            System.out.println("============ 개발자 관리 ============");
            System.out.println("1. 개발자 등록");
            System.out.println("2. 전체 목록 보기");
            System.out.println("3. 이름으로 검색");
            System.out.println("0. 종료");

            String menuNumStr =  sc.nextLine();

            try {
                int menuNum =  Integer.parseInt(menuNumStr);

                switch (menuNum) {
                    case 1:
                        registerDeveloper();
                        break;
                    case 2:
                        printDevList();
                        break;
                    case 3:
                        searchDeveloperByName();
                        break;
                    case 0:
                        System.out.println("개발자 관리 프로그램을 종료합니다.");
                        return;
                    default:
                        System.out.println("메뉴를 잘못 입력하셨습니다.");
                        continue;
                }
            } catch (NumberFormatException e) {
                System.out.println("숫자를 입력하세요.");
            }
        }
    }
    static void registerDeveloper() {
        System.out.println("============ 개발자 등록 ============");
        System.out.print("이름 : ");
        String name =  sc.nextLine();

        System.out.print("개발분야 [1]MOBILE [2]FRONTEND [3]BACKEND [4]DBA : ");
        String typeStr = sc.nextLine();
        DevType devType = null;
        try {
            int type = Integer.parseInt(typeStr);
            switch (type) {
                case 1:
                    devType = DevType.MOBILE;
                    break;
                case 2:
                    devType = DevType.FRONTEND;
                    break;
                case 3:
                    devType = DevType.BACKEND;
                    break;
                case 4:
                    devType = DevType.DBA;
                    break;
                default:
                    System.out.println("잘못 입력 하셨습니다.");
                    return;
            }
        } catch (NumberFormatException e) {
            System.out.println("숫자를 입력해주세요.");
        }
        System.out.print("경력 [1]신입 [2]경력 : ");
        String careerStr = sc.nextLine();
        Career career = null;
        try {
            int type = Integer.parseInt(careerStr);
            switch (type) {
                case 1:
                    career = Career.JUNIOR;
                    break;
                case 2:
                    career = Career.SENIOR;
                    break;
                default:
                    System.out.println("잘못 입력하셨습니다.");
                    return;
            }
        } catch (NumberFormatException e) {
            System.out.println("숫자를 입력해주세요.");
        }
        System.out.print("성별 [1]남자 [2]여자 : ");
        String genderStr = sc.nextLine();
        Gender gender = null;
        try {
            int type = Integer.parseInt(genderStr);
            switch (type) {
                case 1:
                    gender = Gender.MALE;
                    break;
                case 2:
                    gender = Gender.FEMALE;
                    break;
                default:
                    System.out.println("잘못 입력하셨습니다.");
                    return;
            }
        } catch (NumberFormatException e) {
            System.out.println("숫자를 입력해주세요.");
        }
        System.out.print("주소 : ");
        String addr =  sc.nextLine();

        Developer developer = new Developer(name, devType, career, gender, addr);
        devList.add(developer);
        System.out.println(name + "님 개발자 등록 완료 되었습니다.");
    }

    static void printDevList() {
        System.out.println("============ 전체 목록 조회 ============");
        if (devList.isEmpty()) {
            System.out.println("등록된 개발자가 없습니다.");
        } else {
            for (Developer developer : devList) {
                System.out.println(developer.toString());
            }
        }
    }

    static void searchDeveloperByName() {
        System.out.println("============ 이름으로 검색 ============");
        while (true) {
            System.out.print("이름을 입력해주세요 (종료 > 엔터) : ");
            String name = sc.nextLine();
            boolean found = false;

            if (name.isEmpty()) {
                break;
            }

            for (Developer developer : devList) {
                if (developer.getName().equals(name)) {
                    System.out.println(developer.toString());
                    found = true;
                }
            }

            if (!found) {
                System.out.println(name + " 개발자는 등록되지 않았습니다.");
            }

            if(found) break;
        }
    }
}
