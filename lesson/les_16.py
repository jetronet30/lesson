sl = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "country": "USA",
    "hobbies": ["reading", "traveling", "coding"],
    "is_married": False,
}

del sl["age"]  # dict-ის ელემენტის წაშლა key-ის მიხედვით
print(sl)

if "age" in sl:
    print("Age is in the dictionary")
    del sl["age"]
else:
    print("Age is not in the dictionary")


print("------------------")
slov_9 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "country": "USA",
    "hobbies": ["reading", "traveling", "coding"],
    "is_married": False,
}
print(slov_9)

slov_10 = slov_9.pop(
    "age", "Age is not in the dictionary"
)  # dict.pop() - dict-ის ელემენტის წაშლა და მისი მნიშვნელობის დაბრუნება key-ის მიხედვით
print(slov_10)  # 30

print("------------------")

slov_11 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "country": "USA",
    "hobbies": ["reading", "traveling", "coding"],
    "is_married": False,
}
print(slov_11)

slov_12 = (
    slov_11.popitem()
)  # dict.popitem() - dict-ის ელემენტის წაშლა და მისი მნიშვნელობის დაბრუნება
print(slov_12)


print("------------------")
slov_13 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "country": "USA",
    "hobbies": ["reading", "traveling", "coding"],
    "is_married": False,
}


print(
    slov_13.get("age", "Age is not in the dictionary")
)  # dict.get() - dict-ის ელემენტის მნიშვნელობის დაბრუნება key-ის მიხედვით, თუ key არ არსებობს, დაბრუნდება default მნიშვნელობა
print(
    slov_13.get("height", "Height is not in the dictionary")
)  # დაბრუნდება default მნიშვნელობა


print("------------------")
slov_14 = {
    "name": "SUzie",
    "age": 23,
    "city": "Atlanta",
    "country": "USA",
    "hobbies": ["reading", "traveling", "coding"],
    "is_married": False,
}

print(
    slov_14.setdefault("age", 30)
)  # dict.setdefault() - dict-ის ელემენტის მნიშვნელობის დაბრუნება key-ის მიხედვით, თუ key არ არსებობს, შექმნის ახალ key-value წყვილს და დააბრუნებს default მნიშვნელობას
print(
    slov_14.setdefault("height", 170)
)  # key არ არსებობს, ამიტომ შეიქმნება ახალი key-value წყვილი და დაბრუნდება default მნიშვნელობა
print(slov_14)


print("------------------")
slov_15 = {
    "name": "Alice",
    "age": 25,
    "city": "Boston",
    "country": "USA",
    "hobbies": ["reading", "traveling", "coding"],
    "is_married": True,
}
slov_15.update(
    {"age": 26, "city": "Chicago"}
)  # dict.update() - dict-ის ელემენტების დამატება ან განახლება key-value წყვილების მიხედვით
print(slov_15)


print("------------------")
slov_16 = {
    "name": "Bob",
    "age": 30,
    "city": "Los Angeles",
    "country": "USA",
    "hobbies": ["reading", "traveling", "coding"],
    "is_married": False,
}

print(slov_16.keys())
print(slov_16.values())
print(slov_16.items())  # dict_items - dict-ის key-value წყვილების

for key, value in slov_16.items():
    print(key, value)

print(len(slov_16))


print("------------------")

slov_17 = {
    "name": "Bob",
    "age": 30,
    "city": "Los Angeles",
    "country": "USA",
    "hobbies": ["reading", "traveling", "coding"],
    "is_married": False,
}

print(dict(sorted(slov_17.items())))


print("------------------")

telephone = {
    "John": {"home": 123456789, "mobile": 987654321, "city": "New York"},
    "Alice": {"home": 987654321, "mobile": 555128312, "city": "San Francisco"},
    "Bob": {"home": 123456789, "mobile": 987654321, "city": "Los Angeles"},
}
print(telephone["John"]["home"])
print(telephone["Alice"]["mobile"])
print(telephone["Bob"]["city"])

for key, value in telephone.items():
    print(key, value)
