// 1. Print Numbers
function printNumbers() {
  for (let index = 1; index <= 10; index++) {
    console.log(index);
  }
}
// 2. Reverse Counting
function reverseCounting() {
  for (let index = 10; index >= 1; index--) {
    console.log(index);
  }
}
// 3. Even Numbers
function evenNumbers() {
  for (let index = 2; index <= 20; index += 2) {
    console.log(index);
  }
}
// 4. Odd Numbers
function oddNumbers() {
  for (let index = 1; index <= 20; index += 2) {
    console.log(index);
  }
}
// 5. Sum of Numbers
function sumOfNumbers() {
  let sum = 0;
  for (let index = 1; index <= 10; index++) {
    sum += index;
  }
  console.log(sum);
}
// 6. FizzBuzz
function fizzBuzz() {
  for (let index = 1; index <= 100; index++) {
    if (index % 3 === 0 && index % 5 === 0) {
      console.log("FizzBuzz");
    } else if (index % 3 === 0) {
      console.log("Fizz");
    } else if (index % 5 === 0) {
      console.log("Buzz");
    } else {
      console.log(index);
    }
  }
}
var items = [1, 2, 3,4];
items.concat;
console.log(items);
