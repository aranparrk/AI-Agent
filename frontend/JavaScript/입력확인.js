const prompt = require('prompt-sync')();

// 나이 입력 받기
// let age = parseInt(prompt('나이 입력 : '), 10);

// if (isNaN(age)) {
//   console.log('숫자를 입력해야 함');
// } else if (age > 19) {
//   console.log(`당신의 나이는 ${age}살 이고, 성인입니다.`);
// } else {
//   console.log(`당신의 나이는 ${age}살 이고, 미성년자입니다.`);
// }

// 이름, 나이, 성별, 주소, 국어, 영어, 수학 성적을 입력 받음
// 이름, 나이, 성인여부, 주소, 총점, 평균 출력하기
/*
let name = prompt('이름 입력 : ');
let age = parseInt(prompt('나이 입력 : '), 10);
let gender = prompt('성별 입력 : ');
let addr = prompt('주소 입력 : ');
let koreanScore = parseInt(prompt('국어 성적 입력 : '), 10);
let englishScore = parseInt(prompt('영어 성적 입력 : '), 10);
let mathScore = parseInt(prompt('수학 성적 입력 : '), 10);

let totalScore = koreanScore + englishScore + mathScore;
let avgScore = (totalScore / 3).toFixed(1);

console.log('='.repeat(65));
console.log(`이름은 ${name} 이고, `);

if (age > 19) {
  console.log(`나이는 ${age}살이고, 성인 입니다.`);
} else {
  console.log(`나이는 ${age}살이고, 미성년자 입니다.`);
}

console.log(`성별은 ${gender} 이고, ${addr}에 거주 중입니다.`);
console.log(`성적의 총점은 ${totalScore}이고 평균은 ${avgScore}입니다.`);
console.log('='.repeat(65));
*/

// 연산자 : 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/), 나머지(%), 거듭제곱(**)
// const x = 10;
// const y = 4;

// console.log(x + y);
// console.log(x - y);
// console.log(x * y);
// console.log(x / y);
// console.log(Math.trunc(x / y));
// console.log(x % y);
// console.log(x ** y);

// 분을 입력 받아 시/분 구하기
// 350분을 입력하면 5시간 50분
// console.log('='.repeat(50));
// const totalMinute = parseInt(prompt('분을 입력하세요 : '), 10);

// if (isNaN(totalMinute)) {
//   console.log('숫자를 입력해야 함');
// } else {
//   const hour = Math.trunc(totalMinute / 60);
//   const minutes = totalMinute % 60;

//   console.log('='.repeat(50));
//   console.log(`입력하신 시/분은 ${hour}시간 ${minutes}분입니다.`);
// }
// console.log('='.repeat(50));

// 3자리 정수를 입력 받아 100의 자리, 10의 자리, 1의 자리 값을 출력
// 586 => 100의 자리 5, 10의 자리 8, 1의 자리 6
// const num = parseInt(prompt('3자리 정수를 입력하세요 : '), 10);
// console.log('='.repeat(50));

// let oneHundreds = 0
// let tens = 0
// let ones = 0

// if (isNaN(num)) {
//   console.log('숫자를 입력해야 함');
// } else if (num < 100 || num > 999) {
//   console.log('3자리 정수가 아님');
// } else {
//   oneHundreds = Math.trunc(num / 100);
//   tens = Math.trunc((num % 100) / 10);
//   ones = num % 10;

//   console.log(`100의 자리 ${oneHundreds}, 10의 자리 ${tens}, 1의 자리 ${ones}`);
// }

// 조건문을 이용해 가장 큰 수 출력
// if (oneHundreds > tens) {
//   if(oneHundreds > ones) {
//     console.log(oneHundreds);
//   } else {
//     console.log(ones);
//   }
// } else { 
//   if (tens > ones) {
//     console.log(tens);
//   } else {
//     console.log(ones);
//   }
// }

// console.log('='.repeat(50));

// 단항 연산자 : 항이 1개인 연산자
// let z = 100;

// console.log(z++);
// console.log(z);

// console.log(++z);
// console.log(z);

// console.log('='.repeat(50));

// 대입 연산자 : 좌편에 있는 변수에 값을 대입 (=)
// +=, -=, *=, /=, %=
// let a = 10;

// console.log(a); // 10
// console.log(a += 2); // 12, a = a + 2
// console.log(a -= 2); // 10, a = a - 2
// console.log(a *= 2); // 20, a = a * 2
// console.log(a /= 2); // 10, a = a / 2
// console.log(a %= 2); // 0

// console.log('='.repeat(50));

// 비교연산자 : 두 개의 피연산자를 비교해 참과 거짓을 반환
// let b = 10;
// let c = 20;

// console.log(b == c); // false
// console.log(b >= c); // false
// console.log(b < c); // true
// console.log(b <= c); // true
// console.log(b != c); // true

// console.log('='.repeat(50));

// let xx = 10;
// let yy = '10';

// console.log(xx === yy); // 일치 연산자

// 논리연산자 : and(&&), or(||), not(!)
let x = 10;
let y = 20;

console.log(x > 5 && x > y); // false
console.log(x > 5 || x > y); // true
console.log(!(x > 5 || x > y)); // false

// ===================================================================
// JS 코드 작성 시 정리 노트 (원본 코드 리뷰 기반)
// ===================================================================

// -------------------------------------------------------------------
// 1. parseInt(문자열, 10) — 두 번째 인자(radix, 진법)
// -------------------------------------------------------------------
// - 두 번째 인자는 몇 진법으로 해석할지 지정하는 것
// - 생략해도 요즘 브라우저는 대부분 10진법으로 처리하지만,
//   옛날 엔진에서는 '0'으로 시작하는 문자열을 8진법으로 오인식하는
//   버그가 있었음 → parseInt('08') → 0 이 나오는 경우 존재
// - 명시 안 하면 "의도적으로 뺀 건지 실수인지" 코드 읽는 사람이
//   구분 못 함 → 습관적으로 항상 10 붙이기
//   예: parseInt('08', 10) // 항상 8


// -------------------------------------------------------------------
// 2. isNaN() — 입력 검증
// -------------------------------------------------------------------
// - 값이 NaN(Not a Number)인지 검사
// - 사용자가 숫자 아닌 값을 입력하면 parseInt/Number가 NaN 반환
// - NaN인 채로 비교 연산하면 항상 false 나옴 → 에러 없이 조용히
//   틀린 결과가 출력되는 게 제일 위험
//   예: parseInt('스무살') → NaN
//       NaN > 19 → false (미성년자로 잘못 판별됨, 에러 안 뜸)
// - 사용자 입력을 숫자로 변환한 후에는 항상 isNaN으로 걸러줄 것
//   예: if (isNaN(age)) { console.log('숫자를 입력해야 함'); }


// -------------------------------------------------------------------
// 3. 삼항연산자 (조건 ? A : B)
// -------------------------------------------------------------------
// - if/else를 한 줄로 줄이는 문법
// - if/else는 "구문"(코드 블록), 삼항연산자는 "표현식"(값)이라서
//   변수 할당이나 템플릿 리터럴 안에 바로 넣을 수 있음
//   예: const status = age > 19 ? '성인' : '미성년자';
// - 조건이 딱 2가지로 갈리고 결과를 바로 대입/출력할 때만 사용
// - 조건 3개 이상이거나 로직 복잡하면 중첩하지 말고 if/else 사용
//   (중첩 삼항연산자는 가독성 나빠짐)


// -------------------------------------------------------------------
// 4. Math.floor vs Math.trunc vs parseInt(숫자에 사용)
// -------------------------------------------------------------------
// - Math.floor(7.9)  → 7   (내림, 음수는 더 작은 값으로: -7.9 → -8)
// - Math.trunc(7.9)  → 7   (소수점만 자름, 음수도 방향 무시: -7.9 → -7)
// - parseInt(7.9)    → 7   (동작은 하지만 원래 "문자열→숫자" 변환용
//                            함수라 숫자에 쓰는 건 목적에 안 맞는 도구)
// - 양수만 다루면 셋 다 결과 같음, 실무 영향 없음
// - 의도 명확히 하려면: 숫자 계산 버림 → Math.floor/trunc,
//                       문자열 변환 → parseInt로 역할 분리


// -------------------------------------------------------------------
// 5. toFixed(n) — 반올림 + 문자열 변환
// -------------------------------------------------------------------
// - 소수점 n자리까지 반올림해서 "문자열"로 반환
//   예: (89.666).toFixed(1) → "89.7"
// - Math.floor(89.666) → 89 (그냥 버림, 숫자 반환) 과 다름
// - 성적 평균처럼 반올림이 관례에 맞는 경우 toFixed가 더 현실적
//   (버리면 89.9점도 89점 처리되어 손해)
// - 주의: 반환값이 문자열이라 추가 연산하려면 Number()/parseFloat()로
//   다시 변환 필요. 화면 출력만 할 거면 상관없음


// -------------------------------------------------------------------
// 6. '문자열'.repeat(n)
// -------------------------------------------------------------------
// - 문자열을 n번 반복해서 이어붙임
//   예: '='.repeat(5) → "====="
// - 구분선(=====) 직접 세어서 타이핑하는 대신 사용
// - 길이 바꿀 때 숫자만 수정하면 되므로 유지보수 편함


// -------------------------------------------------------------------
// 7. parseInt vs Number — 입력값 숫자 변환
// -------------------------------------------------------------------
// [parseInt(문자열, 10)]
// - 정수만 필요할 때 사용 (나이, 성적, 개수 등)
// - 문자열 앞부분부터 읽다가 숫자 아닌 문자 나오면 거기까지만 파싱
//   예: parseInt('123abc') → 123
// - 소수점 있어도 무조건 버림: parseInt('123.45') → 123
// - 빈 문자열은 NaN → 최소한 미입력은 걸러짐: parseInt('') → NaN
//
// [Number(문자열)]
// - 소수까지 정확히 받아야 할 때 사용 (키, 몸무게, 가격 등)
// - 문자열 전체가 완전히 숫자로 변환 가능해야 함, 하나라도
//   이상하면 통째로 NaN: Number('123abc') → NaN
// - 소수점 그대로 살림: Number('123.45') → 123.45
// - ⚠️ 빈 문자열은 0으로 취급 (버그 유발 포인트)
//   Number('') → 0 → 사용자가 아무것도 안 쳐도 에러 없이 0 들어감
//
// [선택 기준]
// - 정수 필요 (나이, 성적)        → parseInt(값, 10)
// - 소수 필요 (키, 가격)          → Number(값)
// - 지저분한 입력에서 앞부분만 뽑고 싶음 → parseInt
// - 전체 유효성 엄격 검사 필요      → Number
// - 어느 쪽이든 변환 후 isNaN()으로 검증 필수
// ===================================================================