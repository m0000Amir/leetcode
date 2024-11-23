function onionWrapper(stringOrFunction) {
  let cities = [];
  let f;

  cities.push(stringOrFunction)


  return function curried(...args) {
    if (!args.length) {
      f && f(cities);
    }

    if (typeof args[0] === 'function') {
      f = args[0];
    }

    if (typeof args[0] === 'string') {
      let city = args[0];
      if (f) {
        cities = cities.filter((item) => item !== city);
      } else {
        cities.push(city);
      }
    }

    return curried;
  };
}

module.exports = onionWrapper;

const taxFunc = (...args) => console.log(args)

const a = onionWrapper('city1')('city2')('cityN')(taxFunc)
a('city1')();

// function curry(f) { // curry(f) выполняет каррирование
//   return function(a) {
//     return function(b) {
//       return f(a, b);
//     };
//   };
// }
//
// // использование
// function sum(a, b) {
//   return a + b;
// }
//
// let curriedSum = curry(sum);
//
// console.log( curriedSum(1)(2) ); // 3


