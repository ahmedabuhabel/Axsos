function accsingElements() {
  let colors = ["red", "blue", "green", "yellow", "purple"];
  console.log(colors[0]);
  console.log(colors[colors.length - 1]);
}
function traversing() {
  let numbers = [10, 20, 30, 40, 50];
  for (let index = 0; index < numbers.length; index++) {
    console.log(numbers[index]);
  }
  for (let index = numbers.length - 1; index >= 0; index--) {
    console.log(numbers[index]);
  }
}
function searchingArray() {
  let numbers = [5, 10, 15, 20, 25];
  if (numbers.includes(25)) {
    console.log("Found at position " + numbers.indexOf(25));
  } else {
    console.log("Not found");
  }
}
searchingArray();
