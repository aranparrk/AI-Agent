package 커피메뉴만들기;

// Menu Class 만들기
public class MenuInfo {
    private String name;            // 이름
    private int price;              // 가격
    private String category;        // 분류
    private String desc;            // 설명
    private boolean isTax;          // 세금 여부

    // 매개변수가 전부 포함된 생성자 만들기
    public MenuInfo(String name, int price, String category, String desc, boolean isTax) {
        this.name = name;
        this.price = price;
        this.category = category;
        this.desc = desc;
        this.isTax = isTax;
    }

    // Getter / Setter 만들기
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    public boolean isTax() {
        return isTax;
    }

    public void setTax(boolean tax) {
        isTax = tax;
    }

    // toString() 오버라이딩해서 정보 출력
    @Override
    public String toString() {
        return String.format("이름 : %-10s | 가격 : %d | 카테고리 : %-5s | 설명 : %s | 세금 : %s ",
                name, price, category, desc, (isTax ? "포함" : "미포함"));
    }
}
