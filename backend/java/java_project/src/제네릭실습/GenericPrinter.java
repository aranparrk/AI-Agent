package 제네릭실습;

public class GenericPrinter<T> {
    private T material;

    public T getMaterial() {
        return material;
    }

    public void setMaterial(T material) {
        this.material = material;
    }
    @Override  // 문법적으로 오버라이드 관계가 성립하는지 확인 하는 용도
    public String toString() {  // Object Class에서 가지고 있는 메서드 오버라이딩
        return material.toString();
    }
}

// 재료가 분말
class Power {
    public void doPrinting() {
        System.out.println("Power 재료로 출력 합니다.");
    }
    @Override
    public String toString() {
        return "재료는 Power 입니다.";
    }
}

// 재료가 플라스틱
class Plastic {
    public void doPrinting() {
        System.out.println("Plastic 재료로 출력 합니다.");
    }
    @Override
    public String toString() {
        return "재료는 Plastic 입니다.";
    }
}

// 재료가 Nylon
class Nylon {
    public void doPrinting() {
        System.out.println("Nylon 재료로 출력 합니다.");
    }
    @Override
    public String toString() {
        return "재료는 Nylon 입니다.";
    }
}