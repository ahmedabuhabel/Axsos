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
function sortingArray() {
  let scores = [50, 20, 70, 10, 40];
  console.log(scores.sort((a, b) => a - b));
  console.log(scores.sort((a, b) => b - a));
  let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];
  console.log(names.sort());
}
function insertingElements() {
  let animals = ["dog", "cat", "rabbit"];
  animals.push("elephant");
  animals.unshift("lion");
  animals.splice(2, 0, "tiger");

  console.log(animals);
}

function removingElements() {
  let fruits = ["apple", "banana", "cherry", "date"];

  fruits.shift();
  fruits.pop();
  fruits.splice(fruits.indexOf("banana"), 1);
  console.log(fruits);
}
function combineArrays() {
  let array1 = [1, 2, 3];
  let array2 = [4, 5, 6];
  let combinedArray = [];
  combinedArray = combinedArray.concat(...array1, array2);
  console.log(combinedArray);
}
function splittingArrays() {
  let items = ["a", "b", "c", "d", "e"];
  let array1 = items.slice(0, 3);
  let array2 = items.slice(2, items.length);
  console.log(array1);
  console.log(array2);
}
function filteringElements() {
  let numbers = [1, 5, 10, 15, 20, 25, 30];
  let filterdArray = [];
  for (let index = 0; index < numbers.length; index++) {
    if (numbers[index] > 15) {
      filterdArray.push(numbers[index]);
    }
  }
  console.log(filterdArray);
}
function removeDuplicates() {
  let input = [1, 2, 2, 3, 3, 4, 4, 5];
  let distinctArray = [];
  for (let i = 0; i < input.length; i++) {
    if (distinctArray.includes(input[i])) {
      continue;
    } else {
      distinctArray.push(input[i]);
    }
  }
  console.log(distinctArray);
}
function rotateArray(arr, k) {
  arr = [1, 2, 3, 4, 5];
  k = 2;
  let rotatedArray = [];
  let slicedArray = arr.slice(arr.length - k, arr.length);
  let remainingArray = arr.slice(0, arr.length - k);
  rotatedArray = rotatedArray.concat(slicedArray, remainingArray);
  console.log(rotatedArray);
}
function sortedArray(arr1, arr2) {
  let result = [];
  let i = 0;
  let j = 0;
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      result.push(arr1[i]);
      i++;
    } else {
      result.push(arr2[j]);
      j++;
    }
  }
  while (i < arr1.length) {
    result.push(arr1[i]);
    i++;
  }

  while (j < arr2.length) {
    result.push(arr2[j]);
    j++;
  }
  return result;
}
function longestCommonPrefix(strs) {
  if (strs.length === 0) return "";

  let res = "";

  for (let i = 0; i < strs[0].length; i++) {
    let char = strs[0][i];

    for (let j = 1; j < strs.length; j++) {
      if (i >= strs[j].length || strs[j][i] !== char) {
        return res;
      }
    }

    res += char;
  }

  return res;
}

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
