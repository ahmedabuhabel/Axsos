console.log("page loaded...");
function changeName() {
  let userName = document.querySelector("#userName");
  userName.innerText = "Ahmed Abuhabel";
}
function removeRequest(element) {
  let request = element.parentElement;
  request.remove();
  decreaseRequests();
}
function decreaseRequests() {
  let badge = document.querySelector(".badge");
  badge.innerText = parseInt(badge.innerText) - 1;
}
function icreaseNumberOfConnections() {
  let numberOfConnections = document.querySelector("#connections");
  numberOfConnections.innerText = parseInt(numberOfConnections.innerText) + 1;
}
