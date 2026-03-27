function alwaysHungry(arr) {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "food") {
      console.log("Yummy");
      count++;
    }
  }
  if (count === 0) {
    console.log("I'm hungry");
  }
}
function highPass(arr, cutoff) {
  var filteredArr = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > cutoff) {
      filteredArr.push(arr[i]);
    }
  }
  return filteredArr;
}
function betterThanAverage(arr) {
  var sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  let average = sum / arr.length;

  var count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > average) {
      count++;
    }
  }
  return count;
}
function reverse(arr) {
  let reverseArray = [];
  for (let i = arr.length - 1; i >= 0; i--) {
    reverseArray.push(arr[i]);
  }
  return reverseArray;
}

function fibonacciArray(n) {
  var fibArr = [0, 1];
  for (let i = 2; i < n; i++) {
    let nextFib = fibArr[i - 1] + fibArr[i - 2];
    fibArr.push(nextFib);
  }
  return fibArr;
}
