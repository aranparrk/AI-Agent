package 리모콘인터페이스;

// interface 키워드를 사용해 인터페이스 작성
// 인터페이스(Interface)는 클래스가 구현해야 할 메서들의 명세(specification)를 정의한 설계 명세
// 인터페이스는 "이런 기능을 제공해야 한다"는 규칙 또는 약속의 정의
// 이를 통해 다양한 클래스가 동일한 기능을 일관된 형식으로 구현
// 자바는 클래스의 다중 상속을 허용하지 않지만, 인터페이스는 다중 구현이 가능
public interface RemoteControl {
    int MAX_VOLUME = 100; // 자동으로 public static final이 추가됨
    int MIN_VOLUME = 0;

    void turnOn(); // 자동으로 public abstract가 추가됨, 즉 모든 메서드가 추상메서드
    void turnOff();
    void setVolume(int volume);
    int getVolume();
}
