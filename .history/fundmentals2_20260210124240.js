function countdown(input) {
  let result = [];
  for (let index = input; index >= 0; index--) {
    result.push(index);
  }
  console.log(result);
  return result;
}
countdown(10);
