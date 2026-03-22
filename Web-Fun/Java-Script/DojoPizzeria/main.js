function pizzaOven(typeOfPizza, typeOfCrust, typeOfCheeses, pizzaToppings) {
  var pizza = {};
  pizza.typeOfPizza = typeOfPizza;
  pizza.typeOfCrust = typeOfCrust;
  pizza.typeOfCheeses = typeOfCheeses;
  pizza.pizzaToppings = pizzaToppings;
  return pizza;
}
function randomPizza() {
  var randomPizza = {};
  var typeOfPizza = ["hand tossed", "deep dish"];
  var typeOfCrust = ["traditional", "marinara"];
  var typeOfCheeses = ["mozzarella", "feta"];
  var pizzaToppings = ["pepperoni", "sausage", "mushrooms", "olives", "onions"];
  randomPizza.typeOfPizza =
    typeOfPizza[Math.floor(Math.random() * typeOfPizza.length)];
  randomPizza.typeOfCrust =
    typeOfCrust[Math.floor(Math.random() * typeOfCrust.length)];
  randomPizza.typeOfCheeses =
    typeOfCheeses[Math.floor(Math.random() * typeOfCheeses.length)];
  randomPizza.pizzaToppings =
    pizzaToppings[Math.floor(Math.random() * pizzaToppings.length)];

  return randomPizza;
}
var pizza1 = pizzaOven(
  "deep dish",
  "traditional",
  ["mozzarella"],
  [("pepperoni", "sausage")],
);
var pizza2 = pizzaOven(
  "hand tossed",
  "marinara",
  ["mozzarella", "feta"],
  ["mushrooms", "olives", "onions"],
);

console.log(randomPizza());
