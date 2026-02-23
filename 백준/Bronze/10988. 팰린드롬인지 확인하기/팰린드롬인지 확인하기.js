let fs = require("fs");
let str = fs.readFileSync("/dev/stdin").toString().trim();


function solution(str) {
  let len = str.length;
  let mid = 0;

  if (len % 2 == 0) {
    mid = len / 2;
    let test1 = str.slice(mid).split("").reverse().join("");
    let test2 = str.slice(0, mid);
    if (test1 === test2) console.log(1);
    else console.log(0);
  } else {
    mid = Math.floor(len / 2);
    let test1 = str
      .slice(mid + 1)
      .split("")
      .reverse()
      .join("");
    let test2 = str.slice(0, mid);
    if (test1 === test2) console.log(1);
    else console.log(0);
  }
}


solution(str);
