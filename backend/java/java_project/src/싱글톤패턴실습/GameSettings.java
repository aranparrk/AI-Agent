package 싱글톤패턴실습;


public class GameSettings {
    String resolution;
    int volume;
    String difficulty;

    private static GameSettings gameSetting = new GameSettings();

    private GameSettings() {
        resolution =  "1920x1080";
        volume = 20;
        difficulty = "NORMAL";
    }

    static GameSettings getInstance() {
        return gameSetting;
    }


}
