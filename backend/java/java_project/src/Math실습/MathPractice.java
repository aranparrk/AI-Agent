package Math실습;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MathPractice {
    public static void main(String[] args) {
        practice1();
        System.out.println(practice2(10.111, 2));
        practice3(95, 10);
        practice4(1, 2, 4,6);
        practice5();
    }

    // ============================================================
    // [실습 1] 주사위 시뮬레이션 (random)
    // 주사위 2개를 10,000번 굴려서 두 눈의 합(2~12)이 각각 몇 번 나왔는지 출력하세요.
    // 결과를 보고 어떤 합이 가장 많이 나오는지 확인해 봅시다. (예상: 7)
    // ============================================================
    static void practice1() {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < 10000; i++) {
            int dice1 = (int)(Math.random() * 6 + 1);
            int dice2 = (int)(Math.random() * 6 + 1);

            list.add(dice1 + dice2);
        }

        int maxCount = 0;
        int maxSum = 0;

        for (int i = 2; i <= 12; i++) {
            int count = Collections.frequency(list, i);

            if (count > maxCount) {
                maxCount = count;
                maxSum = i;
            }
        }

        System.out.println("가장 많이 나온 합 : " + maxSum);
    }
    // ============================================================
    // [실습 2] 원하는 자리에서 반올림하기 (round, pow)
    // Math.round()는 항상 정수로 반올림합니다.
    // 실수 value를 소수점 digits 자리까지 반올림하는 메서드 roundTo(value, digits)를 만드세요.
    //   roundTo(3.14159, 2) -> 3.14
    //   roundTo(2.71828, 3) -> 2.718
    // 추가 질문: Math.round(-10.5)의 결과는? (-11이 아니라 -10)
    // ============================================================
    static double practice2(double value, int digits) {
        double pow = Math.pow(10, digits);
        double roundTo = Math.round(value * pow) / pow;

        return roundTo;
    }
    // ============================================================
    // [실습 3] 게시판 페이지 수 계산 (ceil)
    // 전체 게시글 수와 한 페이지에 보여줄 글 수가 주어질 때, 총 페이지 수를 구하세요.
    //   게시글 95개, 페이지당 10개 -> 10페이지
    //   게시글 100개, 페이지당 10개 -> 10페이지
    //   게시글 0개 -> 0페이지
    // 함정: Math.ceil(95 / 10) 은 왜 9.0이 나올까요? (정수 나눗셈이 먼저 일어남)
    // ============================================================
    static void practice3(int board, int page) {

        int pageNum = (int)Math.ceil((double)board / page);

        System.out.println("게시글 " + board + "개, 페이지당 " + page + " -> " +  pageNum + "페이지");
    }
    // ============================================================
    // [실습 4] 두 점 사이의 거리 (abs, sqrt, pow)
    // 좌표 (x1, y1), (x2, y2)가 주어질 때 두 가지 거리를 구하세요.
    //   - 맨해튼 거리 : |x1 - x2| + |y1 - y2|
    //   - 유클리드 거리 : √((x1 - x2)² + (y1 - y2)²)
    //   (1, 2) ~ (4, 6) -> 맨해튼 7, 유클리드 5.0
    // ============================================================
    static void practice4(int x1, int y1, int x2, int y2) {
        int manhattan = Math.abs(x1 - x2) + Math.abs(y1 - y2);
        double euclidean = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));

        System.out.println("(" +  x1 + "," + y1 + ") ~ (" + x2 + "," + y2 + ") -> 맨해튼 " + manhattan + ", 유클리드 " + euclidean);
    }
    // ============================================================
    // [실습 5] 성적 처리 (random, max, min, round 종합)
    // 1. 학생 10명의 점수를 0~100 사이 임의의 값으로 생성해 리스트에 저장하세요.
    // 2. Math.max / Math.min 을 사용해 최고점과 최저점을 구하세요. (Collections 사용 금지)
    // 3. 평균을 소수점 첫째 자리까지 반올림해 출력하세요. (실습 2의 roundTo 활용)
    // 4. 최고점과 최저점을 뺀 나머지 8명의 평균도 구하세요.
    // ============================================================
    static void practice5() {
        List<Integer> student = new ArrayList<>();
        int score = 0;
        int scoreMax = 0;
        int scoreMin = 101;
        int scoreTotal = 0;

        for (int i = 0; i < 10; i++) {
            score = (int)(Math.random() * 101);
            student.add(score);

            scoreMax = Math.max(scoreMax, score);
            scoreMin = Math.min(scoreMin, score);

            scoreTotal += score;
        }

        double scoreAvg = (double)scoreTotal / student.size();
        scoreAvg = practice2(scoreAvg, 1);

        student.remove(Integer.valueOf(scoreMax));
        student.remove(Integer.valueOf(scoreMin));

        int totalScore = 0;

        for (int i = 0; i < student.size(); i++) {
            totalScore += student.get(i);
        }

        double avgScore = (double)totalScore / student.size();
        avgScore = practice2(avgScore, 1);

        System.out.println("최고점 : " + scoreMax);
        System.out.println("최저점 : " + scoreMin);
        System.out.println("평균 : " + scoreAvg);
        System.out.println("나머지 평균 : " + avgScore);
    }
}