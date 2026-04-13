x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]
x[1][0] = 15
x[0][1] = 1
print(x)
students[0]["last_name"] = "Brayant"
sports_directory["soccer"][0] = "Andres"


z[0]["y"] = 30


def iterateDictionary(some_list):
    for item in some_list:
        print(f"first_name - {item['first_name']}, last_name - {item['last_name']}")


def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(f"{item[key_name]}")


def printInfo(some_dict):
    for key in some_dict:
        values = some_dict[key]
        print(len(values), key)

        for item in values:
            print(item)


dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
}
printInfo(dojo)
