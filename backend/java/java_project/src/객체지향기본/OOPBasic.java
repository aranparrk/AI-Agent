package 객체지향기본;

public class OOPBasic {
    public static void main(String[] args) {
        Television tv = new Television();

        tv.setPower(true);
        tv.setChannel(30, true);
        tv.setBrand("삼성");
        tv.setVolume(50);

        tv.showTelevision();
    }
}
