class Animal:
    def __init__(self, name, age, health=100, happiness=50):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}")

        print(f"Health: {self.health}")
        print(f"Happiness: {self.happiness}")

        return self

    # increase the health and happiness when feeding the animal
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self

    def feed(self, amount):
        pass


class Lion(Animal):

    def feed(self):
        super().feed()
        self.happiness += 5


class Zebra(Animal):

    def feed(self):
        super().feed()
        self.health += 20


class Tiger(Animal):

    def feed(self):
        super().feed()
        self.health += 10


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    # Here I use Polymorphism instead of adding Lion - Tiger in seperated functions
    def add_Animal(self, animal):
        self.animals.append(animal)

    # Here when I call it will feed all animals based on animal type
    def feed_all(self):
        for animal in self.animals:
            animal.feed()

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_Animal(Lion("Nala", 15))
zoo1.add_Animal(Lion("Simba", 15))
zoo1.add_Animal(Tiger("Rajah", 15))
zoo1.add_Animal(Tiger("Shere Khan", 15))
zoo1.feed_all()
zoo1.print_all_info()
