package 싱글톤패턴실습;

public class Player {
    private String name;
    GameSettings gameSetting = GameSettings.getInstance();

    public Player(String name) {
        this.name = name;
    }

    void setSetting(String resolution, int volume, String difficulty) {
        System.out.println(name + "의 설정변경");
        gameSetting.setResolution(resolution);
        gameSetting.setVolume(volume);
        gameSetting.setDifficulty(difficulty);
    }

    void viewSettings() {
        System.out.println(name + "의 현재 설정");
        System.out.println("해상도 : " + gameSetting.getResolution());
        System.out.println("볼륨 : " + gameSetting.getDifficulty());
        System.out.println("난이도 : " + gameSetting.getVolume());

    }
}
