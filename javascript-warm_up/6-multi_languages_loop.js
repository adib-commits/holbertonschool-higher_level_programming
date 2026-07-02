#!/usr/bin/node

const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let output = '';
let i = 0;

while (i < languages.length) {
  output += languages[i];
    output += '\n';

  i++;
}

console.log(output);
