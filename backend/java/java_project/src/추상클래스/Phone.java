package 추상클래스;

// abstract 키워드로 추상 클래스 생성 : 인스턴스화 안 됨(즉, 객체 생성 불가)
public abstract class Phone {
    public String name;
    public boolean isPower;

    public Phone(String name) {
        this.name = name;
    }

    public void setPower(boolean isPower) {
        this.isPower = isPower;
        if (isPower) {
            System.out.println("Phone Power ON");
        } else {
            System.out.println("Phone Power OFF");
        }
    }

    abstract void call(); // 추상메서드는 구현부가 없으므로 상속받은 자식 클래스에서 반드시 오버라이딩 해야 함
    abstract void store();
}
