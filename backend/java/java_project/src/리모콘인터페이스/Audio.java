package 리모콘인터페이스;

public class Audio implements RemoteControl {
    private int volume;
    @Override
    public void turnOn() {
        System.out.println("오디오를 켭니다");
    }

    @Override
    public void turnOff() {
        System.out.println("오디오를 끕니다");
    }

    @Override
    public void setVolume(int volume) {
        if (volume > RemoteControl.MAX_VOLUME) {
            volume = RemoteControl.MAX_VOLUME;
        } else if (volume < RemoteControl.MIN_VOLUME) {
            volume = RemoteControl.MIN_VOLUME;
        } else{
            this.volume = volume;
        }
        System.out.println("현재 오디오 볼륨은 " + this.volume + "입니다.");
    }

    @Override
    public int getVolume() {
        return this.volume;
    }
}
