package 회원정보예제;

import java.util.Scanner;

public class Member {
    private String name; // 인스턴스 필드, 객체 생성 시 함께 생성 됨
    private int age; // private은 클래스 내부에서만 접근 가능한 접근 제한자
    private char gender;
    private int job;
    private final Scanner sc = new Scanner(System.in);

    // 이름 설정하기, 세터
    public void setName() { // void : return값이 없음
        System.out.println("이름 : ");
        name = sc.nextLine();
    }

    // 이름 가져오기
    public String getName() {
        return name;
    }

    // 나이 설정하기
    public void setAge() {
            while (true) {
                System.out.println("나이 : ");
                String ageStr = sc.nextLine();
                try {
                    age = Integer.parseInt(ageStr);
                    if(age >= 0 && age < 200) break;
                    System.out.println("나이 입력 범위가 아닙니다.");
                } catch (NumberFormatException e) {
                    System.out.println("숫자만 입력하세요.");
                }
            }
        }
    // 나이 가져 오기
    public int  getAge() {
        return age;
    }

    public void setGender() {
        while(true) {
            System.out.println("성별 : ");
            gender = sc.next().charAt(0);
            if (gender == 'f' || gender == 'm') break;
            else System.out.println("성별을 잘못 입력 하셨습니다.");
        }
    }

    public char getGender() {
        return gender;
    }

    public void setJob() {
        while(true) {
            System.out.println("직업 : ");
            String jobStr = sc.nextLine();
            try {
                job = Integer.parseInt(jobStr);
                if (job >= 1 && job <= 4) break;
                System.out.println("직업을 다시 입력 해주세요");
            } catch (NumberFormatException e) {
                System.out.println("숫자만 입력하세요.");
            }
        }
    }

    public int getJob() {
        return job;
    }

    public void getInfo() {
        // final은 최종 값을 의미 함(상수)
        final String[] jobStr = {"", "학생", "회사원", "주부", "무직"};
        System.out.println("=".repeat(7) + "회원 정보" + "=".repeat(7));
        System.out.println("이름 : " + name);
        System.out.println("나이 : " + age);
        System.out.println("성별 : " + ((gender == 'm' ? "남성" : "여성")));
        System.out.println("직업 : " + jobStr[job]);
    }

}
