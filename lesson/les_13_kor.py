import timeit
# kor = 23,45,11,78, 'hello', 'world'
# print(type(kor))
# print(kor)

# x ,y, z, a, b, c, *t = 1, 34, 56, 78, 'hi', 'python', 23,45,11,78, 'hello', 'world'
# print(x)
# print(y)
# print(z)
# print(a)
# print(b)
# print(c)
# print(t)

# print('------------------')

# l = 5
# j = 10
# print(l, j)
# l, j = j, l
# print(l, j)


kor_1 = (23, 45, 11, 78, "hello", "world")
print(11 in kor_1)
print(100 in kor_1)

v_kor_1 = (23, 45, 11, 78, ("java", "python"), "hello", "world")
print(v_kor_1[4][1])


print("------------------")

kor_2 = (23, 45, 11, 78, "hello", "world", [78, 90])
# kor_2[4] = 'c++'  not allowed
kor_2[6][0] = 100
print(kor_2)

print("------------------")

kor_3 = (1, 2, 3, 4)
kor_4 = (5, 6, 7, 8)
print(kor_3 > kor_4)

for i in kor_3:
    print(i)

# del kor_3
# print(kor_3)  # NameError: name 'kor_3' is not defined
kor_5 = 2, 8, 1, 9
print(sorted(kor_5))

print(kor_5.count(""))
print(kor_5.index(8))

print("------------------")
kor_6 = (1, 2, 3, 4)
kor_7 = (5, 6, 7, 8)
print(kor_6)
print(list(kor_6))
print(tuple(kor_6))

print(kor_6 + kor_7)

print(timeit.timeit('x=(1, 2, 3, 4, 5)'))
print(timeit.timeit('x=[1, 2, 3, 4, 5]'))