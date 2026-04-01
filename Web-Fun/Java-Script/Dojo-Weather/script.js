console.log("page loaded...");
function removeCookie(element) {
  let cookie = element.parentElement;
  cookie.remove();
}
function convertUnit() {
  let unit = document.querySelector("#temp");
  let max = document.querySelectorAll(".max-degreee");
  let min = document.querySelectorAll(".min-degreee");
  if (unit.value === "f") {
    max.forEach((el) => {
      let temp = parseInt(el.innerText);
      el.innerText = Math.round((temp * 9) / 5 + 32);
    });

    min.forEach((el) => {
      let temp = parseInt(el.innerText);
      el.innerText = Math.round((temp * 9) / 5 + 32);
    });
  } else {
    max.forEach((el) => {
      let temp = parseInt(el.innerText);
      el.innerText = Math.round(((temp - 32) * 5) / 9);
    });

    min.forEach((el) => {
      let temp = parseInt(el.innerText);
      el.innerText = Math.round(((temp - 32) * 5) / 9);
    });
  }
}
document.querySelector("#temp").addEventListener("change", convertUnit);
function showAlert(element) {
  alert(element.innerText);
}
