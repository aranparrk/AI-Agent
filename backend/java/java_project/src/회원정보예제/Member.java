package 회원정보예제;

import java.util.Scanner;

public class Member {
    String name;
    int age;
    char gender;
    int job;
    Scanner sc = new Scanner(System.in);

    public void setName() {
        System.out.println("이름 : ");
        name = sc.nextLine();
    }

    public String getName() {
        return name;
    }

    public void setAge() {
        while(true){
            System.out.println("나이 : ");
            age = sc.nextInt();
            if(0 < age && age < 200) break;
            else System.out.println("나이를 잘못 입력 하셨습니다. 다시 입력하세요/");

            }
        }

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
            job = sc.nextInt();
            if (job == 1 || job == 2 || job == 3 || job == 4) break;
            else System.out.println("직업을 다시 입력 해주세요");
        }
    }

    public int getJob() {
        return job;
    }

    public void getInfo() {
        final String[] jobStr = {"", "학생", "회사원", "주부", "무직"};
        System.out.println("=".repeat(7) + "회원 정보" + "=".repeat(7));
        System.out.println("이름 : " + name);
        System.out.println("나이 : " + age);
        System.out.println("성별 : " + ((gender == 'm' ? "남성" : "여성")));
        System.out.println("직업 : " + jobStr[job]);
    }

}
