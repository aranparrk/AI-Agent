package 추상클래스;

public class AndroidPhone extends Phone {

    public AndroidPhone(String name) {
        super(name); // 부모의 생성자 호출, 자식클래스의 생성자 호출 시 부모 생성자를 머저 불러 줘야 함
    }

    @Override
    void call() {
        System.out.println("부모의 요청으로 안드로이드 폰에 통화 기능을 구현 합니다.");
    }

    @Override
    void store() {
        System.out.println("구글스토어 기능입니다.");
    }
}
