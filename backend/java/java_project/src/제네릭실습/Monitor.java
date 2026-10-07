package 제네릭실습;

public class Monitor extends Device{

    @Override
    public void turnOn() {
        System.out.println("모니터 전원을 켭니다.");
    }

    @Override
    public void turnOff() {
        System.out.println("모니터 전원을 끕니다.");
    }
}
