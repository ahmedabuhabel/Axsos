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
function longestCommonPrefix(strs) {
  if (strs.length === 0) {
    return "";
  }

  let prefix = strs[0];

  for (let i = 1; i < strs.length; i++) {
    while (!strs[i].startsWith(prefix)) {
      prefix = prefix.slice(0, prefix.length - 1);

      if (prefix === "") {
        return "";
      }
    }
  }

  return prefix;
}
longestCommonPrefix(["flower", "flow", "fly"]);
function changeBackgroundColor() {
  let color = document.querySelector(".btn");
  console.log(color);
  color.style.backgroundColor = "red";
  console.log("Pressed");
}
