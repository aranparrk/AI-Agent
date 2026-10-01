package 싱글톤;

// 싱글톤(Singleton) : 하나만 생성된다고 해서 이 객체를 싱글톤이라 부름
// - Spring Boot의 Spring Container에 bean 등록이 싱글톤임
// - 이미 생성된 인스턴스를 활용하기 때문에 속도나 메모리 측면에서 이득
// - 코드가 복잡해지고, 동시성 문제를 해결하기위해 synchronized를 사용해야 하는 경우가 있음

public class SingleMain {
    public static void main(String[] args) {
        Student student1 = new Student();
        Student student2 = new Student();

        student1.setInfo("원이", 3000);

        student1.print();
        student2.print();
    }
}
