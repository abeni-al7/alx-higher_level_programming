#!/usr/bin/node
const args = process.argv;
if (args.length <= 4) {
  console.log(0);
} else {
  let max = Number(args[2]);
  for (let i = 3; i < args.length; i++) {
    const num = Number(args[i]);
    args[i] = Number(args[i]);
    if (num > max) {
      max = num;
    }
  }
  let secondMax = Number(args[2]);
  for (let i = 3; i < args.length; i++) {
    const num = Number(args[i]);
    if (num === max) {
      continue;
    }
    if (num > secondMax) {
      secondMax = num;
    }
  }
  console.log(secondMax);
}
