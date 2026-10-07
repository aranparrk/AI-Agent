package 자바API;

// 자바API : 자바에서 제공하는 다양한 API이며, 라이브러리라고 부르기도 함
// JDK에서 제공하는 많은 클래스를 활용하면 프로그램을 더욱 효율적으로 구현
// java.lang 패키지 : 자바에서 가장 기본적인 동작을 수행을하는 클래스들의 집합 (import가 필요 없음)
// - Object : 자바의 최상위 클래스, 11개의 메서드를 가짐
// java.util 패키지 : 자바에서 두 번째로 많이 사용하는 클래스들의 집합 (import 필요)


public class APIMain {
    public static void main(String[] args) {
        Student student1 = new Student("장원영", 1000);
//        Student student2 = student1;
        Student student2 = new Student("장원영", 2000);

        System.out.println(student1); // toString()을 하지 않아도 메서드는 생략 가능, 객체의 정보를 문자열(클래스명@16진수해시코드)로 반환
        System.out.println(student2.equals(student1)); // 두 객체가 같은지 비교
        System.out.println(student1.name.equals(student2.name)); // 문자열은 String 클래스에서 문자열 비교로 오버라이딩 해둠

    }
}

class Student extends Object{
    String name;
    int id;

    @Override
    public String toString() {
        return "이름 : " + name + ", 아이디 : " + id + "\n";
    }

    Student(String name, int id) {
        this.name = name;
        this.id = id;
    }

    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
}

