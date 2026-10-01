package 싱글톤패턴실습;

public class Player {
    GameSettings gameSetting = GameSettings.getInstance();

    void setSetting(String resolution, int volume, String difficulty) {
        gameSetting.resolution = resolution;
        gameSetting.volume = volume;
        gameSetting.difficulty = difficulty;
    }

    void print() {
        System.out.println(gameSetting.difficulty);
        System.out.println(gameSetting.volume);
        System.out.println(gameSetting.resolution);
    }
}
