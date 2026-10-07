package 매개변수다형성;

public class Vehicle {
    public void run() {
        System.out.println("차량이 달립니다.");
    }
}

class SportsCar extends Vehicle {
    @Override
    public void run() {
        System.out.println("스포츠카가 달립니다.");
    }
}

class Sedan extends Vehicle {
    @Override
    public void run() {
        System.out.println("자동차가 달립니다.");
    }
}

class Truck extends Vehicle {
    @Override
    public void run() {
        System.out.println("트럭이 달립니다.");
    }
}