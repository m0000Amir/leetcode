// Для чтения входных данных в Node.js необходимо использовать
// модуль readline, который работает с потоком ввода-вывода
// (stdin/stdout) и позволяет читать строки.
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Данные во входном потоке могут состоять из нескольких строк.
// Чтобы прочитать их, можно использовать метод rl.on(),
// который вызывается каждый раз при появлении новой строки
// в потоке ввода.
// Чтобы вывести результат в поток вывода (stdout),
// можно использовать метод console.log().
// Пример:
// console.log('Результат:', result);

rl.on('line', line => {
  function solve(n, m, i, j, mem) {
    if (mem[i][j] < 0){
      let ans = 0;
      if (i < n-2 && j < m-1) {
        ans += solve(n, m, i+2, j+1, mem);
      }
      if (i < n-1 && j < m-2) {
        ans += solve(n,m, i+1, j+2, mem);
      }
      mem[i][j] = ans;
    }
    return mem[i][j]
  }
  const [N, M] = line.split(' ').map(Number);
  let mem = new Array(N);            // создаем пустой массив длины `M`
  for (let i = 0; i < N; i++) {
    mem[i] = new Array(M).fill(-1);        // делаем каждый элемент массивом
  }
  mem[N-1][M-1] = 1;


  solve(N, M, 0, 0, mem);
  console.log(solve(N, M, 0, 0, mem));

 rl.close();
});


