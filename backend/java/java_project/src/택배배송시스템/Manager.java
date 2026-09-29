package 택배배송시스템;

public class Manager {
    public void send(Delivery d) {
        System.out.println(d.company + "회사가 배송을 시작합니다.");
        d.deliver();
    }
}
