package 영화표예매하기;

public class MovieTicket {
    private final int[] seat = new int[10]; // 좌석 10개의 상태를 저장하는 배열
    private final int price;

    // 생성자를 통해서 가격을 주입 받음
    public MovieTicket(int price) {
        this.price = price;
    }

    // 좌석 상태 출력 : 1이면 예약 좌석 [V], 0이면 예약되지 않은 좌석 [ ]
    // for문을 순회하면서 값을 확인해서 출력
    public void printSeat() {
        int cnt = 0;

        for (int e : seat) {
            System.out.print(e == 0 ? "[ ]" : "[V]");
            cnt++;

            if (cnt == 5) {
                System.out.println();
                cnt = 0;
            }
        }
    }

    // 좌석 예매 메서드
    // 먼저 좌석상태를 보여주기 위해서 좌석 상태 출력 메서드 호출 이후 예매(0이면 예약 안 된 좌석, 1이면 예약된 좌석)
    public void selectSeat(int seatNum) {
        if (!isValidSeat(seatNum)) {
            System.out.println("존재하지 않는 좌석입니다.");
            return;
        }

        if (seat[seatNum - 1] == 0) {
            seat[seatNum - 1] = 1;
            System.out.printf("%d번 좌석 예매 성공하였습니다.%n", seatNum);
            printSeat();
        } else {
            System.out.printf("%d번 좌석은 이미 예매된 좌석입니다.%n", seatNum);
        }
    }

    // 예약 취소 메서드
    public void cancelSeat(int seatNum) {
        if (!isValidSeat(seatNum)) {
            System.out.println("존재하지 않는 좌석입니다.");
            return;
        }

        if (seat[seatNum - 1] == 1) {
            seat[seatNum - 1] = 0;
            System.out.printf("%d번 좌석이 취소되었습니다.%n", seatNum);
            printSeat();
        } else {
            System.out.printf("%d번 좌석은 이미 비어있는 좌석입니다.%n", seatNum);
        }
    }

    // 총 판매 금액 반환 메서드 (int형으로 반환)
    public int totalAmount() {
        int total = 0;

        for (int e : seat) {
            if (e == 1) {
                total += price;
            }
        }

        return total;
    }

    // 좌석 유효 범위 체크 메서드
    private boolean isValidSeat(int seatNum) {
        return seatNum >= 1 && seatNum <= seat.length;
    }
}