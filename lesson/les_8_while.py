import time

# x = 0

# while x <= 10:
#     print(x)
#     x += 1
#     time.sleep(1)

# x = y = 1

# while x < 10:
#     while y < 10:
#         print(x, '*', y, '=', x * y, end=' | ')
#         y += 1
#     print()
#     y = 1
#     x += 1

number =  int(input("enter num : "))

s = 0

while number:
    s += number % 10
    number //= 10

print(s)
