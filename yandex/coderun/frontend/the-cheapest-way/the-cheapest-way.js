// Для чтения входных данных в Node.js необходимо использовать
// модуль readline, который работает с потоком ввода-вывода
// (stdin/stdout) и позволяет читать строки.
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  });

// Данные во входном потоке могут состоять из нескольких строк.
// Чтобы прочитать их, можно использовать метод rl.on(),
// который вызывается каждый раз при появлении новой строки
// в потоке ввода.
// Чтобы вывести результат в поток вывода (stdout),
// можно использовать метод console.log().
// Пример:
// console.log('Результат:', result);

// Пример решения задачи "Вычислите сумму A+B":
// rl.on('line', line => {
// const [a, b] = line.split(' ').map(Number);
//  console.log(a + b);
//  rl.close();
// });

rl.on('line', line => {
  const [N, M] = line.split(' ').map(Number);
  let weight = new Array(N);
  for (let i = 0; i < N; i++) {
    let row = line.split(' ').map(Number);
    weight[i] = row.slice(0, M);
  }
  console.log(weight);
  rl.close();
  // if (counter === 0) {
  //   n = Number(line);
  //   counter += 1;
  // } else {
  //   points = line.split(' ').map(Number);
  //   points = points.slice(0, n);
  //   counter += 1;
  // }
  // if (counter >= 2) {
  //   rl.close();
  //   getMinLength();
  // }
});
