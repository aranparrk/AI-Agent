package 추상클래스;

public class AbstractMain {
    public static void main(String[] args) {
        Phone phone1 = new AndroidPhone("갤럭시 S25");
        phone1.call();
        phone1.store();

        Phone phone2 = new ApplePhone("iPhone 15");
        phone2.call();
        phone2.store();

    }
}
