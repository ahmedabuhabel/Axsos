function ReverseString(str) {
  str = "hello";

  var reversed = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }
  console.log(reversed);
}

function countVowels(str) {
  var count = 0;

  for (let i = 0; i < str.length; i++) {
    switch (str[i]) {
      case "a":
      case "e":
      case "i":
      case "o":
      case "u":
      case "A":
      case "E":
      case "I":
      case "O":
      case "U":
        count++;
        break;
    }
  }
  console.log(count);
}

function palindrome() {
  let str = "madam";

  let reversed = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }

  let i = 0;
  while (i < str.length) {
    if (str[i] !== reversed[i]) {
      return false;
    }
    i++;
  }

  return true;
}
function longestWordInString(str) {
  var words = str.split(" ");
  var longest = words[0];
  for (var i = 1; i < words.length; i++) {
    if (words[i].length > longest.length) {
      longest = words[i];
    }
  }
  return longest;
}
function grade(score) {
  switch (score) {
    case "A":
      return "Excellent";

    case "B":
      return "Good job";

    case "C":
      return "You passed";

    case "D":
      return "Need improvement";

    case "F":
      return "Failed";

    default:
      return "Invalid grade";
  }
}
function countCharacters(str) {
  var vowels = 0;
  var digits = 0;
  var spaces = 0;
  var others = 0;
  for (var i = 0; i < str.length; i++) {
    switch (str[i]) {
      case "a":
      case "e":
      case "i":
      case "o":
      case "u":
      case "A":
      case "E":
      case "I":
      case "O":
      case "U":
        vowels++;
        break;
      case " ":
        spaces++;
        break;
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
        digits++;
        break;
      default:
        others++;

        break;
    }
  }
  var output = { vowels, digits, spaces, others };
  return output;
}
