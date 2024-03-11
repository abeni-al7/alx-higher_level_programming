#!/usr/bin/node
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let max = Number(args[2]);
  let secondMax = Number(args[3]);

  if (secondMax > max) {
    [max, secondMax] = [secondMax, max];
  }

  for (let i = 4; i < args.length; i++) {
    const num = Number(args[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax) {
      secondMax = num;
    }
  }

  console.log(secondMax);
}
