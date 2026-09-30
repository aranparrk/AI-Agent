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
        animalList.add(new Animal());
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
            if (animal instanceof Human h){
                h.readBook();
            } else if (animal instanceof Tiger t){
                t.hunting();
            } else if (animal instanceof Eagle e){
                e.flying();
            } else if (animal instanceof Dog d){
                d.playing();
            } else if (animal instanceof Cat c){
                c.eating();
            } else {
                System.out.println("지원되지 않는 형입니다.");
            }
        }
    }
}

