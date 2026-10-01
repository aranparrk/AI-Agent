package 싱글톤패턴실습;

public class GameMain {
    public static void main(String[] args) {
        Player player1 = new Player();
        Player player2 = new Player();

        player1.setSetting("300X400", 50, "HARD");

        player1.print();
        player2.print();

    }
}
