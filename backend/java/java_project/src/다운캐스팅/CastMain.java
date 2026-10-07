package 다운캐스팅;
// 다운캐스팅이란, 상위 클래스 타입(부모 타입)으로 선언된 객체를 다시 하위 클래스 타입(자식 타입)으로 형변환하는 것

import java.util.ArrayList;
import java.util.List;

public class CastMain {
    List<Animal> animalList = new ArrayList<>();
    public static void main(String[] args) {
        CastMain castMain = new CastMain();

        castMain.addAnimal();
        castMain.downCast();
    }

    public void addAnimal(){
        animalList.add(new Human());
        animalList.add(new Tiger());
        animalList.add(new Eagle());
        animalList.add(new Dog());
        animalList.add(new Cat());

        for (Animal animal : animalList){
            animal.move();
        }
    }

    public void downCast() {
        for (Animal animal : animalList){
            animal.move();
            animal.option();
        }
    }
}

