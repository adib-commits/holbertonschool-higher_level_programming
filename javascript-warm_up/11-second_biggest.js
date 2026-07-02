#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const max = Math.max(...args);
  let second = -Infinity;

  for (let i = 0; i < args.length; i++) {
    if (args[i] > second && args[i] < max) {
      second = args[i];
    }
  }

  console.log(second);
}
