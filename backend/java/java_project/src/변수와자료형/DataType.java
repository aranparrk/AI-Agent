package 변수와자료형;

public class DataType {
    public static void main(String[] args) {
        boolean isTrue = true; // 참과 거짓 구분 용도, 1byte
        char gender = 'M'; // 문자 저장, 자바에 문자는 '', 문자열 "", 문자는 내부적으로 정수값으로 사용 됨, 부호 없는 2byte
        String name = "박아란"; // 문자열을 저장, 참조 타입
        byte bVar = 120; // 1byte, -128 ~ 127
        short sVar = 30000; // 2byte, -32768 ~ 32767
        int iVar = 1000000; // 4byte, -2147483648 ~ 2147483647
        long lVar = 1000000000L; // 8byte, -9223372036854775808 ~ 9223372036854775807
        float fVar = 3.14f; // 4byte
        double dVar = 3.14; // 8byte

        // 묵시적 형변환 : 컴파일로 자동으로 형변환을 하는 것
        int num = 10;
        double dNum = 20.13;
        double rst = num + dNum; // 묵시적 형변환이 일어남, 유리한 방향으로 더 큰 데이터 타입으로 변환 됨
        System.out.println(rst);

        // 명시적 형변환 : 사용자가 의도를 가지고 형변환을 하는 것
        int kor = 66;
        int math = 33;
        int eng = 77;
        double avg = (double)(kor + math + eng) / 3; // 58.66, (dobule)을 하거나 3.0을 하거나, 명시적 형변환과 묵시적 형변환이 함께 일어남
        System.out.println(avg); // 58.0, 정수 / 정수 였으니까

    }
}
