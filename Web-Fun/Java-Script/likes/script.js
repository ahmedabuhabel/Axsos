function increment(element) {
  let card = element.parentElement;
  let numberOfLikes = card.querySelector(".likes");
  numberOfLikes.innerText = parseInt(numberOfLikes.innerText) + 1;
}
