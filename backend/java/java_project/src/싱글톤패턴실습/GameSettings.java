package 싱글톤패턴실습;


public class GameSettings {
    private String resolution;
    private int volume;
    private String difficulty;

    public String getDifficulty() {
        return difficulty;
    }

    public int getVolume() {
        return volume;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }

    public void setDifficulty(String difficulty) {
        this.difficulty = difficulty;
    }

    public String getResolution() {
        return resolution;
    }

    // 클래스 생성시 단 한 번 객체 생성
    private static GameSettings gameSetting = new GameSettings();

    // 외부에서 new로 생성하지 못하도록 private 생성
    private GameSettings() {
        resolution =  "1920x1080";
        volume = 20;
        difficulty = "NORMAL";
    }

    // 유일한 인스턴스 반환
    static GameSettings getInstance() {
        return gameSetting;
    }

}
