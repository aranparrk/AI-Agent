package 제네릭;

// 제네릭(Generic)은 데이터 타입을 일반화하여, 다양한 타입의 데이터를 하나의 코드로 처리할 수 있도록 해주는 자바의 기능
// - 컴파일 시 타입을 지정타입 안정성(type safety) 확보
// - 불필요한 형변환(casting) 제거

public class GenericMain {
    public static void main(String[] args) {
        Person<String> p1 = new Person<>("장원영");
        System.out.println(p1.getInfo());

        Person<Integer> p2 = new Person<>(1004);
        System.out.println(p2.getInfo());
    }
}

class Person<T> {
    T info;

    Person(T info) {
        this.info = info;
    }

    public T getInfo() {
        return info;
    }
}
