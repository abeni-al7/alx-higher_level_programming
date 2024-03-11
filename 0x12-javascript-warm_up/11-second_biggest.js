#!/usr/bin/node
const args = process.argv;
if (args.length <= 4) {
  console.log(0);
} else {
  let max = 0;
  for (let i = 2; i < args.length; i++) {
    args[i] = Number(args[i]);
    if (args[i] > max) {
      max = i;
    }
  }
  let secondMax = 0;
  for (let i = 2; i < args.length; i++) {
    if (i === max) {
      continue;
    }
    args[i] = Number(args[i]);
    if (args[i] > secondMax) {
      secondMax = args[i];
    }
  }
  console.log(secondMax);
}
