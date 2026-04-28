slov = {"name": "John", 
        "age": 30, 
        "city": "New York",
        "country": "USA",
        "hobbies": ["reading", "traveling", "coding"],
        "is_married": False,}
print(type(slov)) # <class 'dict'>  dict - კილიტიანი კოლექცია, რომელიც შედგება key-value წყვილებისგან
print(slov)

slov_1 = dict(name="Alice", age=25, city="Los Angeles")
print(slov_1)

print(slov["name"])
print(slov.get("age"))
print(slov.get("gender", "Not specified"))  # key არ არსებობს, ამიტომ დაბრუნდება default მნიშვნელობა

for key, value in slov.items() :
    print(key,"=", value)


print("------------------")
slov_2=[["apple", 1], ["banana", 2], ["orange", 3]]
print(type(slov_2))  # <class 'list'>  list - რიგის კოლექცია, რომელიც შეიძლება შეიცავდეს სხვადასხვა ტიპის ელემენტებს
slov_3 = dict(slov_2)
print(slov_3)

print("------------------")
slov_4 = ('ab', 'cd', 'ef')
print(type(slov_4))  # <class 'set'>  set - არალაგებული, უნიკალური ელემენტების კოლექცია
slov_4 = dict(slov_4)
print(slov_4)

print("------------------")
slov_5 = {i: i ** 2 for i in range(1,10)}
print(slov_5)

print("------------------")
st = "hello world"
slov_6 = {i: st.count(i) for i in set(st)}  # set comprehension - უნიკალური სიმბოლოების ნაკრები სტრინგიდან
print(slov_6)

print("------------------")
s1 = [1, 2, 3, 4, ]
s2 = ['one', 'two', 'three', 'four']
sl = dict(zip(s1, s2))  # zip - ორი კოლექციის ელემენტების წყვილებად შეკვრა
print(sl)

print("------------------")
slov_7 = dict.fromkeys(['a', 'b', 'c'], 0,)  # fromkeys - ახალი dict-ის შექმნა, სადაც key-ები მოცემული iterable-ის ელემენტებია და value-ები ერთნაირი
print(slov_7)


print("------------------")
slov_8 = {"name": "John", 
          "age": 30, 
          "city": "New York"}
print(slov_8["age"])  # dict_keys - dict-ის key-ების კოლექ
print(slov_8["city"])  # KeyError: 'country' - dict-ში ასეთი key არ არსებობს
print(slov_8.get("country", "Not specified"))  # dict.get() -
print(slov_8.keys())  # dict_keys - dict-ის key-ების კოლექცია
print(slov_8.values())  # dict_values - dict-ის value-ების კოლექცია
print(slov_8.items())  # dict_items - dict-ის key-value წყვილების

slov_8["name"] = "Suzie"  # dict-ის value-ის შეცვლა key-ის მიხედვით
print(slov_8)

slov_8["country"] = "USA"  # dict-ის value-ის შეცვლა key-ის მიხედვით
print(slov_8)


