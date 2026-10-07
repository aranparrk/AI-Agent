package 싱글톤패턴실습;

public class GameMain {
    public static void main(String[] args) {
        // 플레이어 객체 2개 생성
        Player player1 = new Player("원이");
        Player player2 = new Player("리브");

        // 현재 설정 상태 확인
        player1.viewSettings();
        player2.viewSettings();
        System.out.println("=".repeat(30));
        // 플레이어 1 설정 변경
        player1.setSetting("200x400", 50, "EASY");
        System.out.println("=".repeat(30));
        // 플레이어 2 설정 확인
        player2.viewSettings();

    }
}
