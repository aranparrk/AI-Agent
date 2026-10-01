package 싱글톤;

public class Singleton {
    String name;
    int id;
    // 전역변수에 싱글톤 객체를 생성해서 대입, 전역변수는 프로그램 종료시까지 사라지지 않음
    private static Singleton singleton = new Singleton();

    private Singleton() { // 외부에서 생성자 호출을 막기 위해서
        name = "박아란";
        id = 100;
    }

    static Singleton getInstance() { // 외부 호출시 미리 만들어진 싱글톤 객체의 주소를 반환
        return singleton;
    }
}
