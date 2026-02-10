function settingAndSwapping() {
  var myNumber = 42;
  var MyName = "Ahmed";
  var temp = "";
  temp = myNumber;
  myNumber = MyName;
  MyName = temp;
  console.log(myNumber);
  console.log(MyName);
}
function printNumbers() {
  for (let index = -52; index <= 1066; index++) {
    console.log(index);
  }
}
function beCheerful() {
  for (let index = 0; index < 98; index++) {
    console.log("good morning!");
  }
}
function multipleOfThree() {
  for (let index = -300; index <= 0; index++) {
    if (index === -3 || index === -6) {
      continue;
    }
    if (index % 3 === 0) {
      console.log(index);
    }
  }
}
function printIntWithWhile() {
  var i = 2000;
  while (i <= 5280) {
    console.log(i);
    i++;
  }
}
function birthday(input1, input2, day, month) {
  if (
    (input1 === day && input2 === month) ||
    (input1 === month && input2 === day)
  ) {
    console.log("How did you know?");
  } else {
    console.log("Just another day");
  }
}
function leapYear(year) {
  if (year % 400 === 0) {
    return true;
  }
  if (year % 100 === 0) {
    return false;
  }
  if (year % 4 === 0) {
    return true;
  }
  return false;
}
function printAndCount() {
  let counter = 0;
  for (let index = 512; index <= 4096; index++) {
    if (index % 5 === 0) {
      console.log(index);
      counter++;
    }
  }
  console.log("Count: " + counter);
}
function multipleOfSix() {
  for (let index = 0; index <= 6000; index++) {
    if (index % 6 === 0) {
      console.log(index);
    }
  }
}
function CountingTheDojoWay() {
  for (let index = 1; index <= 100; index++) {
    if (index % 5 === 0) {
      console.log("Coding");
      if (index % 10 === 0) {
        console.log("Dojo");
      }
    } else {
      console.log(index);
    }
  }
}
function input(incoming) {
  console.log(incoming);
}
function sumOdds() {
  var sum = 0;
  /*  for (let index = -300000; index <= 300000; index++) {
    if (index % 2 !== 0) {
      sum += index;
    }
  } */
  console.log(sum);
}
function CountdownByFour() {
  let i = 2016;
  while (i > 0) {
    console.log(i);
    i = i - 4;
  }
}
function FlexibleCountdown(lowNumber, highNumber, multiple) {
  for (let index = highNumber; index >= lowNumber; index--) {
    if (index % multiple === 0) {
      console.log(index);
    }
  }
}
function FinalCountdown(lowNumber, highNumber, multiple, excludedNumber) {
  for (let index = highNumber; index >= lowNumber; index--) {
    if (index === excludedNumber) {
      continue;
    }
    if (index % multiple === 0) {
      console.log(index);
    }
  }
}
FinalCountdown(3, 5, 17, 9);
