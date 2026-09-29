package 객체지향기본;

// 상속을 주기 위한 TV
public class ProtoTV {
    boolean isOn; // 인스턴스 필드
    int channel;
    int volume;

    // 생성자
    public ProtoTV() { // 기본 생성자 생성, 생성자는 클래스 이름과 동일, 반환 타입이 존재하지 않음, 클래스가 객체로 만들어 질 때 호출
        this.isOn = false;
        this.channel = 1;
        this.volume = 50;
    }

    // 생성자 오버로딩, 오버로딩은 동일한 이름의 메서드에 대해 매개변수의 개수와 타입으로 구분해서 호출 하는 것, 정적 바인딩이라고 부름
    public ProtoTV(boolean isOn, int channel, int volume) {
        this.isOn = isOn;
        this.channel = channel;
        this.volume = volume;
    }

    public void setChannel(int channel) {
        if (channel >= 1 && channel <= 1000) { // 채널 설정값이 1 ~ 1000까지를 유효값으로 간주
            this.channel = channel; // this는 자기 자신의 객체를 참조하는 변수
        } else {
            System.out.println("채널 설정 범위가 아닙니다.");
        }
    }
}


