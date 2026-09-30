package 추상클래스;

public class ApplePhone extends Phone {

    public ApplePhone(String name) {
        super(name);
    }

    @Override
    public void call() {
        System.out.println("부모의 요청으로 iPhone에 통화 기능을 적용합니다.");
    }

    @Override
    void store(){
        System.out.println("앱스토어 기능입니다.");
    }
}
