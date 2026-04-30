# lamda func

from functools import reduce

message = lambda: print("hello world")

message()


print("------------------")

message_1 = lambda n: n**3

print(message_1(4))

print("------------------")

message_2 = lambda n1, n2: n1 + n2

print(message_2(4, 5))


print("------------------")

products = [
    {"id": 1, "name": "apple", "price": 10},
    {"id": 2, "name": "banana", "price": 5},
    {"id": 3, "name": "orange", "price": 8},
]

print(sorted(products, key=lambda p: p["price"]))

print("------------------")

sp = [[43, 22], [43, 19], [43, 12], [83, 13], [83, 10], [83, 11]]

print(sorted(sp, key=lambda x: x[-1]))


print("------------------")


def my_func(n):
    return lambda x: x * n


print(my_func(100)(15))

print("------------------")

nums = [1, 19, 3, 723, 5, 87, 900, 15, 36]

res = list(filter(lambda x: x >20 , nums))
print(res)

print([i for i in nums if i > 20])


print("------------------")

nums = [1, 19, 3, 723, 5, 87, 900, 15, 36]

res = list(map(lambda x: x ** 2, nums))
print(res)

print([i * 2 for i in nums])


print("------------------")

nums = [1, 19, 3, 723, 5, 87, 900, 15, 36]

res = reduce(lambda a, b: a*b, nums)
print(res)




