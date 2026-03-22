function removeBlanks(str) {
  var strLength = str.length;
  var removedString = "";
  for (let i = 0; i < strLength; i++) {
    if (str[i] !== " ") {
      removedString += str[i];
    }
  }
  console.log(removedString);
}
function getDigits(str) {
  var digit = "";
  for (let i = 0; i < str.length; i++) {
    switch (str[i]) {
      case "0":
      case "1":
      case "2":
      case "3":
      case "4":
      case "5":
      case "6":
      case "7":
      case "8":
      case "9":
        digit += str[i];

        break;

      default:
        break;
    }
  }
  var extractedNumber = Number(digit);

  console.log(extractedNumber);
}
function acronym(str) {
  var splittedWord = str.split(" ");
  var acronymWord = "";
  for (let i = 0; i < splittedWord.length; i++) {
    if (splittedWord[i] === "") {
      continue;
    }
    acronymWord += splittedWord[i][0].toUpperCase();
  }
  console.log(acronymWord);
}
function countNonSpaces(str) {
  var counter = 0;
  for (let index = 0; index < str.length; index++) {
    if (str[index] !== " ") {
      counter++;
    }
  }
  console.log(counter);
}
function removeShorterStrings(arr, minLength) {
  var newArray = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].length >= minLength) {
      newArray.push(arr[i]);
    }
  }
  console.log(newArray);
}
