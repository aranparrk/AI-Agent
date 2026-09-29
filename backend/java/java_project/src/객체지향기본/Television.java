package 객체지향기본;

// ProtoTV로 부터 상속을 받아 Television 클래스 생성
public class Television extends ProtoTV {
    String brand; // 부모가 가지고 있지 않은 것을 추가
    boolean isSmart;


    // 생성자는 클래스가 객체로 만들어질 때 호출 됨
    public Television() {
        super(false, 1, 50); // 하드 코딩
    }

    // 생성자 오버로딩
    public Television(boolean isOn, int channel, int volume) {
        super(isOn, channel, volume); // super()는 부모의 생성자를 호출함, 외부에서 전달 받은 값
    }

    // 전원을 켜고 끄는 메서드 생성
    public void setPower(boolean isOn) {
        this.isOn = isOn;
    }

    public boolean getPower() {
        return this.isOn;
    }

    // 볼륨을 설정하고 볼륨값을 읽는 메서드 생성
    // 볼륨 설정 범위는 0 ~ 100
    public void setVolume(int volume) {
        if (volume >= 0 && volume <= 100) {
            this.volume = volume;
        } else {
            System.out.println("볼륨 범위가 아닙니다.");
        }
    }

    public int getVolume() {
        return this.volume;
    }

    // 부모가 만든 채널 설정을 오버라이딩해서 채널을 1 ~ 2000 늘리기
    @Override // 오버라이딩 관계의 성립 여부를 확인하는 어노테이스
    public void setChannel(int channel) {
        if (channel >= 1 && channel <= 2000) {
            this.channel = channel;
        } else {
            System.out.println("채널 설정 범위가 아닙니다.");
        }
    }

    // 오버라이딩 채널 설정을 오버로딩해서 스마트 기능 구현하기
    public void setChannel(int channel, boolean isSmart) {
        if (isSmart) {
            System.out.println("스마트 TV 모드 입니다.");
            this.isSmart = true;
        } else {
            this.isSmart = false;
            if (channel >= 1 && channel <= 2000) {
                this.channel = channel;
            } else {
                System.out.println("채널 설정 범위가 아닙니다.");
            }
        }
    }

    public int getChannel() {
        return this.channel;
    }

    public boolean isSmart() {
        return this.isSmart;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getBrand() {
        return this.brand;
    }

    // TV 정보 출력하기
    public void showTelevision() {
        System.out.println("전원 : " + isOn);
        System.out.println("채널 : " + channel);
        System.out.println("볼륨 : " + volume);
        System.out.println("브랜드 : " + brand);
        System.out.println("스마트 기능 : " + isSmart);
    }


}
