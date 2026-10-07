package 컬렉션프레임워크;

// 컬렉션프레임워크 : 배열의 단점을 보완하기 위해 만들어짐 (List 계열)
// 데이터 저장 방식과 처리 방법을 구조화하여 클래스로 설계
// 내부 구조가 제네릭
// 자바의 인터페이스 기반 구조, 재사용성, 확장성이 뛰어남

// List : 순서 유지, 중복 허용, ArrayList, LinkedList, Vector, Stack
// Set : 순서 유지 하지 않음, 중복 허용 하지 않음,
// Map : Key-Value 구조, Key중복 허용 하지 않음

import java.util.ArrayList;
import java.util.List;

public class CollectionMain {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        list.add("자바"); // 리스트에 맨 마지막에서 값을 추가
        list.add("C언어");
        list.add("파이썬");
        list.add("리액트");

        System.out.println(list);
        System.out.println(list.get(2)); // 2번 인덱스의 값 추출
        System.out.println(list.size()); // 리스트의 크기를 반환

        for(String s : list) { // 향상된 for 문으로 값을 순회
            System.out.println(s);
        }

    }
}
