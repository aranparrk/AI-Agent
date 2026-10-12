package com.human.mini_prj.repository;

import com.human.mini_prj.constant.ItemSellStatus;
import com.human.mini_prj.entity.Item;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.time.LocalDateTime;
import java.util.List;

@Slf4j
@SpringBootTest
class ItemRepositoryTest {
    @Autowired
    private ItemRepository itemRepository; // 필드를 통한 의존성 주입

    @Test
    @DisplayName("상품 저장 테스트")
    public void createItemTest(){
        for(int i = 1; i < 10; i++){
            Item item = new Item();
            item.setItemNm("테스트 상품" + i);
            item.setPrice(10000 * i);
            item.setItemDetail("테스트 상품 상세 설명" + i);
            item.setStockNumber(100);
            item.setRegTime(LocalDateTime.now());
            item.setUpdateTime(LocalDateTime.now());
            item.setItemSellStatus(ItemSellStatus.SELL);
            Item savedItem = itemRepository.save(item);
            log.info("Item 저장 : {}", savedItem);

        }
    }

    @Test
    @DisplayName("상품 조회 테스트")
    public void findByItemNumTest() {
        this.createItemTest();
        List<Item> itemList = itemRepository.findByItemNm("테스트 상품5");
        for(Item item : itemList){
            log.info("상품 조회 테스트 : {}", item);
        }
    }

    @Test
    @DisplayName("상품명 또는 상품 상세 설명으로 조회")
    public void findByItemNmOrItemDetailTest() {

        // Given : 테스트 데이터 준비
        this.createItemTest();

        // When : 상품 조회
        List<Item> itemList = itemRepository.findByItemNmOrItemDetail(
                "테스트 상품5",
                "테스트 상품 상세 설명3"
        );

        // Then : 결과 확인
        for (Item item : itemList) {
            log.info("조회된 상품 : {}", item);
        }
    }

    @Test
    @DisplayName("가격이 특정 값보다 작은 상품 조회")
    public void findByPriceLessThanTest() {
        this.createItemTest();

        List<Item> itemList = itemRepository.findByPriceLessThan(50000);

        for (Item item : itemList) {
            log.info("조회된 상품 : {}", item);
        }
    }

    @Test
    @DisplayName("가격이 특정 값보다 작은 상품을 가격 내림차순으로")
    public void findByPriceLessThanOrderByPriceDescTest() {
        this.createItemTest();

        List<Item> itemList = itemRepository.findByPriceLessThanOrderByPriceDesc(50000);

        for (Item item : itemList) {
            log.info("조회된 결과 : {}", item);
        }
    }

    @Test
    @DisplayName("가격 범위 검색")
    public void findByPriceBetweenTest() {
        this.createItemTest();

        List<Item> itemList = itemRepository.findByPriceBetween(20000, 50000);

        for (Item item : itemList) {
            log.info("조회된 결과 : {}", item);
        }
    }

    @Test
    @DisplayName("특정 문자열 포함된 상품")
    public void findByItemNmContainingTest() {
        this.createItemTest();

        List<Item> itemList = itemRepository.findByItemNmContaining("5");

        for (Item item : itemList) {
            log.info("조회된 결과 : {}", item);
        }
    }

    @Test
    @DisplayName("판매 상태로 검색")
    public void findByItemSellStatusTest() {
        this.createItemTest();

        List<Item> itemList = itemRepository.findByItemSellStatus(ItemSellStatus.SELL);

        for (Item item : itemList) {
            log.info("조회된 결과 {}", item);
        }
    }

    @Test
    @DisplayName("판매 상태가 같고 가격이 특정 값 이상인 상품")
    public void findByPriceGreaterThanEqualAndItemSellStatusTest() {
        this.createItemTest();

        List<Item> itemList = itemRepository.findByPriceGreaterThanEqualAndItemSellStatus(30000, ItemSellStatus.SELL);

        for (Item item : itemList) {
            log.info("조회된 결과 {}", item);
        }
    }

    @Test
    @DisplayName("가장 비싼 상품 3개")
    public void findTop3ByOrderByPriceDescTest() {
        this.createItemTest();

        List<Item> itemList = itemRepository.findTop3ByOrderByPriceDesc();
        for (Item item : itemList) {
            log.info("조회된 결과 {}", item);
        }
    }

    @Test
    @DisplayName("가격이 목록 중 하나에 해당하는 상품")
    public void findByPriceInTest() {
        this.createItemTest();

        List<Item> itemList = itemRepository.findByPriceIn(List.of(30000, 50000));

        for (Item item : itemList) {
            log.info("조회된 결과 {}", item);
        }
    }

    @Test
    @DisplayName("판매 상태별 상품 개수")
    public void countByItemSellStatusTest(){
        this.createItemTest();

        long count = itemRepository.countByItemSellStatus(ItemSellStatus.SELL);

        log.info("조회된 결과 {}",  count);
    }

    @Test
    @DisplayName("JPQL")
    public void findByItemDetailLikeTest() {
        this.createItemTest();

        List<Item> itemList = itemRepository.findByItemDetailLike("테스트 상품 상세 설명1");

        for (Item item : itemList) {
            log.info("조회된 결과 {}", item);
        }
    }

    @Test
    @DisplayName("native")
    public void findByItemSellStatusNative() {
        this.createItemTest();

        List<Item> itemList = itemRepository.findByItemSellStatusNative("테스트 상품 상세 설명1");

        for (Item item : itemList) {
            log.info("조회된 결과 {}", item);
        }
    }
}