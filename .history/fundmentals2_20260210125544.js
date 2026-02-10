function countdown(input) {
  let result = [];
  for (let index = input; index >= 0; index--) {
    result.push(index);
  }
  return result;
}
function printAndReturn([input1, input2]) {
  console.log(input1);
  return input2;
}
function firstPlusLength(arr) {
  return arr[0] + arr.length;
}
function valuesGreaterThanSecond() {
  let arr = [];
}
function valuesGreaterThanSecondGeneral(arr) {
  let result = [];
  for (let index = 0; index < arr.length; index++) {
    if (arr[index] > arr[1]) {
      result.push(arr[index]);
    }
  }
  return result;
}
