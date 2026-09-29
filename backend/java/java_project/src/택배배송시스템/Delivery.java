package 택배배송시스템;

public class Delivery {
    String company;

    public Delivery(String company) {
        this.company = company;
    }

    public void deliver(){
        System.out.println("배송을 시작합니다.");
    }
}

class ParcelDelivery extends Delivery {
    public ParcelDelivery(String company) {
        super(company);
    }

    @Override
    public void deliver(){
        System.out.println("택배 배송을 시작합니다. 2~3일 소요됩니다.");
    }
}

class QuickDelivery extends Delivery {
    public QuickDelivery(String company) {
        super(company);
    }

    @Override
    public void deliver(){
        System.out.println("퀵 배송을 시작합니다. 당일 도착 예정입니다.");
    }
}

class AirDelivery extends Delivery {
    public AirDelivery(String company) {
        super(company);
    }

    @Override
    public void deliver(){
        System.out.println("항공 배송을 시작합니다. 해외로 출발합니다.");
    }
}