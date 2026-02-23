const [[N, M], ...graph] = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number));

const ex = M - 1;
const ey = N - 1;

const q = [];
q.push([0, 0]);

let isPossible = false;

while (q.length > 0) {
  const [x, y] = q.shift();
  if (x == ex && y == ey) {
    isPossible = true;
  }
  for (const [dx, dy] of [
    [1, 0],
    [0, 1],
  ]) {
    const nx = x + dx;
    const ny = y + dy;
    if (nx < M && ny < N && graph[nx][ny] == 1) {
      q.push([nx, ny]);
      graph[nx][ny] = 0;
    }
  }
}
console.log(isPossible ? "Yes" : "No");