package 문자열리스트;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class ListPractice {
    public static void main(String[] args) {

        List<String> list = new ArrayList<>();
        Scanner sc = new Scanner(System.in);

        // 1. 입력
        System.out.println("=== 1. 문자열 10개 입력 ===");

        for (int i = 0; i < 10; i++) {
            System.out.print((i + 1) + "번째 문자열 입력 : ");
            list.add(sc.nextLine());
        }


        // 2. 전체 출력 및 크기
        System.out.println("\n=== 2. 전체 출력 및 크기 ===");

        System.out.println("리스트 : " + list);
        System.out.println("크기 : " + list.size());


        // 3. 추가
        System.out.println("\n=== 3. 추가 ===");

        list.add("Java");          // 맨 뒤
        list.add(0, "Start");      // 인덱스 0에 삽입

        System.out.println("리스트 : " + list);
        System.out.println("크기 : " + list.size());


        // 4. 조회
        System.out.println("\n=== 4. 조회 ===");

        System.out.println("인덱스 3 : " + list.get(3));


        // 5. 수정
        System.out.println("\n=== 5. 수정 ===");

        String oldValue = list.set(2, "Modified");

        System.out.println("변경 전 값 : " + oldValue);
        System.out.println("변경 후 리스트 : " + list);


        // 6. 삭제
        System.out.println("\n=== 6. 삭제 ===");

        String deleted = list.remove(1);
        System.out.println("삭제된 값 : " + deleted);

        boolean result = list.remove("Java");
        System.out.println("Java 삭제 성공 여부 : " + result);


        // 7. 검색
        System.out.println("\n=== 7. 검색 ===");

        System.out.print("검색어 입력 : ");
        String search = sc.nextLine();

        boolean contains = list.contains(search);

        System.out.println("포함 여부 : " + contains);

        if (contains) {
            System.out.println("인덱스 : " + list.indexOf(search));
        } else {
            System.out.println("찾을 수 없습니다.");
        }


        // 8. 반복 출력
        System.out.println("\n=== 8. 반복 출력 ===");

        for (int i = 0; i < list.size(); i++) {
            System.out.println("[" + i + "] " + list.get(i));
        }


        // 9. 정렬
        System.out.println("\n=== 9. 정렬 ===");

        Collections.sort(list);
        System.out.println(list);


        // 10. 전체 삭제
        System.out.println("\n=== 10. 전체 삭제 ===");

        list.clear();

        System.out.println("크기 : " + list.size());
        System.out.println("비어 있는지 : " + list.isEmpty());

        sc.close();
    }
}