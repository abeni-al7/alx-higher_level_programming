#!/usr/bin/node
function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

const num = Number(process.argv[2]);
let fact = 1;
if (!isNaN(num)) {
  fact = factorial(num);
}
console.log(fact);
