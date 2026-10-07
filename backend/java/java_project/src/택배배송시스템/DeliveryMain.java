package 택배배송시스템;

public class DeliveryMain {
    public static void main(String[] args) {
        Manager m = new Manager();

        ParcelDelivery parcel = new ParcelDelivery("한진택배");
        QuickDelivery quick = new QuickDelivery("CJ대한통운");
        AirDelivery air = new AirDelivery("우체국 택배");

        m.send(parcel);
        m.send(quick);
        m.send(air);
    }
}
