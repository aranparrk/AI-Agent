package 커피메뉴만들기;

import java.util.ArrayList;
import java.util.List;

public class MenuService {
    private final List<MenuInfo> menuList = new ArrayList<>();

    MenuService() {
        initMenu();
    }

    // 초기 메뉴 구성: 5개의 메뉴 객체 생성
    void initMenu() {
        menuList.add(new MenuInfo("아메리카노", 2000, "음료", "기본 커피", true));
        menuList.add(new MenuInfo("아인슈패너", 6500, "음료", "감성 커피", true));
        menuList.add(new MenuInfo("카페라떼", 3000, "음료", "근본 커피", false));
        menuList.add(new MenuInfo("딸기케익", 16500, "디저트", "달콤한 디저트", true));
        menuList.add(new MenuInfo("초코쿠키", 1500, "디저트", "쌉쌀한 디저트", false));
    }

    // 전체 메뉴 조회
    public List<MenuInfo> getAllMenu() {
        return menuList;
    }

    // 메뉴 추가
    public void addMenu(MenuInfo menuInfo) {
        menuList.add(menuInfo);
    }

    // 메뉴 수정
    public boolean updateMenu(int index, MenuInfo menuInfo) {
        if (index >= 0 && index < menuList.size()) {
            menuList.set(index, menuInfo);
            return true;
        }
        return false;
    }

    // 메뉴 삭제
    public boolean deleteMenu(int index) {
        if (index >= 0 && index < menuList.size()) {
            menuList.remove(index);
            return true;
        }
        return false;
    }


    // 메뉴 검색
    public MenuInfo searchMenu(String name) {
        for  (MenuInfo menuInfo : menuList) {
            if (menuInfo.getName().equals(name)) {
                return menuInfo;
            }
        }
        return null;
    }
}
