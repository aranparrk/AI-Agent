package 날짜와시간;

// java.time 패키지 사용


import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class DayTimeMain {
    public static void main(String[] args) {
        LocalDate date = LocalDate.now();               // 오늘 날짜
        LocalTime time = LocalTime.now();               // 현재 시간
        LocalDateTime dateTime = LocalDateTime.now();   // 날짜 + 시간
        ZonedDateTime zoned = ZonedDateTime.now();      // 시간대 포함

        System.out.println(date);       // 2025-05-31
        System.out.println(time);       // 22:38:52.421
        System.out.println(dateTime);   // 2025-05-31T22:38:52.421
        System.out.println(zoned);      // 2025-05-31T22:38:52.421+09:00[Asia/Seoul]

        // 패턴 매칭으로 정보 출력 하기
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        System.out.println(formatter.format(dateTime));

        // 다양한 패턴으로 정보 출력 하기
        // 2026년10월2일
        DateTimeFormatter f1 = DateTimeFormatter.ofPattern("yyyy년M월d일");
        System.out.println(f1.format(dateTime));   // 2026년10월2일
        // 24시간제로 15시50분45초
        DateTimeFormatter f2 = DateTimeFormatter.ofPattern("HH시mm분ss초");
        System.out.println(f2.format(dateTime));   // 15시50분45초
        // 3) 12시간제 + 오전/오후
        DateTimeFormatter f3 = DateTimeFormatter.ofPattern("a hh시 mm분", Locale.KOREAN);
        System.out.println(f3.format(dateTime));   // 오후 03시 50분
        // 4) 요일 포함
        DateTimeFormatter f4 = DateTimeFormatter.ofPattern("yyyy년 MM월 dd일 E요일", Locale.KOREAN);
        System.out.println(f4.format(dateTime));   // 2026년 10월 02일 금요일
        // 5) 밀리초까지
        DateTimeFormatter f8 = DateTimeFormatter.ofPattern("HH:mm:ss.SSS");
        System.out.println(f8.format(dateTime));   // 15:50:45.123
        // 6) 시간대 정보 포함 (ZonedDateTime 사용)
        DateTimeFormatter f11 = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss z (VV)");
        System.out.println(f11.format(zoned));     // 2026-10-02 15:50:45 KST (Asia/Seoul)

    }
}