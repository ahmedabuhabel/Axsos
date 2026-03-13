function printOdd() {
  for (let index = 1; index <= 20; index += 2) {
    console.log(index);
  }
}
function decreasingMultiplesOfThree() {
  for (let index = 100; index >= 0; index--) {
    if (index % 3 === 0) {
      console.log(index);
    }
  }
}
function printSequence() {
  for (let index = 4; index > -4; index += -1.5) {
    console.log(index);
  }
}
function sigma() {
  let sum = 0;
  for (let index = 1; index <= 100; index++) {
    sum += index;
  }
  console.log(sum);
}
function factorial() {
  let product = 1;
  for (let index = 1; index <= 12; index++) {
    product *= index;
  }
  console.log(
    "multiplying 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 = " + product,
  );
}
