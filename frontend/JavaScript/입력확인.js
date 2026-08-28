const prompt = require('prompt-sync')();

// 나이 입력 받기
// let age = parseInt(prompt('나이 입력 : '));

// if (age > 19) {
//   console.log(`당신의 나이는 ${age}살 이고, 성인입니다.`);
// } else {
//   console.log(`당신의 나이는 ${age}살 이고, 미성년자입니다.`);
// }

// 이름, 나이, 성별, 주소, 국어, 영어, 수학 성적을 입력 받음
// 이름, 나이, 성인여부, 주소, 총점, 평균 출력하기
let name = prompt('이름 입력 : ');
let age = parseInt(prompt('나이 입력 : '));
let gender = prompt('성별 입력 : ');
let addr = prompt('주소 입력 : ');
let koreanScore = parseInt(prompt('국어 성적 입력 : '));
let englishScore = parseInt(prompt('영어 성적 입력 : '));
let mathScore = parseInt(prompt('수학 성적 입력 : '));

let totalScore = koreanScore + englishScore + mathScore;
let avgScore = Math.floor(totalScore / 3); // 소숫점 아래 버림

console.log('=================================================================');
console.log(`이름은 ${name} 이고, `);

if(age > 19) {
  console.log(`나이는 ${age}살이고, 성인 입니다.`);
} else {
  console.log(`나이는 ${age}살이고, 미성년자 입니다.`);
}

console.log(`성별은 ${gender} 이고, ${addr}에 거주 중입니다.`);
console.log(`성적의 총점은 ${totalScore}이고 평균은 ${avgScore}입니다.`);
console.log('=================================================================');
