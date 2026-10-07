package 정적멤버;

public class Bank {
    private static int count = 0; // 정적 멤버, 클래스 생성 시 단 한 번 생성
    private static final String NAME =  "KAKAO"; // 정적변수이면서 상수로 정의
    private int account; // 계좌 잔액
    private final String owner; // 예금주

    // 생성자를 통해서 예금주와 잔액을 생성
    public Bank(String owner, int account) {
        this.owner = owner;
        this.account = account;
        count++; // 계좌 개설 갯수 확인용, 정적 멤버
    }

    public static int getCount() {
        return count;
    }

    // 예금
    public void setDeposit(int amount) {
        account += amount;
        System.out.println(amount + "원을 예금 했습니다. 잔액은 " + account + "원 입니다.");
    }

    // 출금
    public void setWithdraw(final int amount) {
        if(account >= amount){
            account -= amount;
            System.out.println(amount + "원을 출금 했습니다. 잔액은 " + account + "원 입니다.");
        } else {
            System.out.println("잔액이 부족합니다. 남은 잔액은 " + account + "원 입니다.");
        }
    }

    // 현재 잔고 확인
    public void printBalance() {
        System.out.println(owner + "님의 현재 잔액은 " + account + "원 입니다.");
    }
}
