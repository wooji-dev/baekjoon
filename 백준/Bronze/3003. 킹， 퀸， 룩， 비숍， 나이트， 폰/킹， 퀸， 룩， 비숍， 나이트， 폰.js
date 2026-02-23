var fs = require("fs");
var input = fs.readFileSync("/dev/stdin").toString().split(" ");

// var input = [3, 4, 1, 1, 1, 6];
let res = [1, 1, 2, 2, 2, 8];


let newArr = input.map((item, idx) => {
	return res[idx] - parseInt(item);
});

console.log(newArr.join(" "));
