let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim();

function solve(str) {
  // 글자 수가 5의 배수가 아니면 절대 불가능
  if (str.length % 5 !== 0) return -1;

  let counts = { q: 0, qu: 0, qua: 0, quac: 0 };
  let curDuck = 0;
  let maxDuck = 0;

  for (let char of str) {
    if (char === "q") {
      counts.q++;
      curDuck++;
      if (curDuck > maxDuck) maxDuck = curDuck;
    } else if (char === "u") {
      if (counts.q > 0) {
        counts.q--;
        counts.qu++;
      } else return -1; // q가 없는데 u가 옴
    } else if (char === "a") {
      if (counts.qu > 0) {
        counts.qu--;
        counts.qua++;
      } else return -1;
    } else if (char === "c") {
      if (counts.qua > 0) {
        counts.qua--;
        counts.quac++;
      } else return -1;
    } else if (char === "k") {
      if (counts.quac > 0) {
        counts.quac--;
        curDuck--;
      } else return -1;
    } else {
      return -1; // quack 외의 이상한 문자
    }
  }

  // 모든 글자를 돌았는데 아직 울고 있는 오리(curDuck)가 있다면 -1
  return curDuck === 0 ? maxDuck : -1;
}

console.log(solve(input));