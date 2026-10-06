package 제네릭실습;

public class GenericEx {
    public static void main(String[] args) {

        // 재료가 분말인 프린터
        GenericPrinter<Power> powerPrinter = new GenericPrinter<>();
        powerPrinter.setMaterial(new Power());
        System.out.println(powerPrinter);  // 자동으로 오버라이딩된 toString() 호출
        powerPrinter.getMaterial().doPrinting();

        // 재료가 플라스틱인 프린터 출력
        GenericPrinter<Plastic> plasticPrinter = new GenericPrinter<>();
        plasticPrinter.setMaterial(new Plastic());
        System.out.println(plasticPrinter);
        plasticPrinter.getMaterial().doPrinting();


        // 재료가 Nylon 프린터 출력
        GenericPrinter<Nylon> nylonPrinter = new GenericPrinter<>();
        nylonPrinter.setMaterial(new Nylon());
        System.out.println(nylonPrinter);
        nylonPrinter.getMaterial().doPrinting();

    }
}