// Для чтения входных данных в Node.js необходимо использовать
// модуль readline, который работает с потоком ввода-вывода
// (stdin/stdout) и позволяет читать строки.
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let counter = 0;
let n;
let points = [];
let dp = [];

const getMinLength = () => {
  if (points.length === 1) {
    console.log(points[0]);
  } else {
    points.sort((a, b) => a - b);
    dp[1] = points[1] - points[0];
    dp[2] = points[2] - points[0];
    for (let i = 3; i < n; i++) {
      dp[i] = Math.min(dp[i-1], dp[i-2]) + points[i] - points[i-1];
    }
    console.log(dp[n-1]);
  }
}

rl.on('line', line => {
  if (counter === 0) {
    n = Number(line);
    counter += 1;
  } else {
    points = line.split(' ').map(Number);
    points = points.slice(0, n);
    counter += 1;
  }
  if (counter >= 2) {
    rl.close();
    getMinLength();
  }
});
