x = 5
listaa = [5]
print(id(x))
print(id(list[0]))


boys = ['Tom', 'Bob', 'Sam']
print(type(boys))
boys.append('Bill')
print(boys.__len__())

sp = list('spam')
print(sp)

numbers = list(range(10))
print(numbers)

nums = [i ** 2 for i in range(100) if i % 2 == 0 and i % 3 == 0]
print(nums)

nums = [i ** 2 if i % 2 == 0  else i ** 3 for i in range(100)]
print(nums)

st = 'spam eggs and spter'
tes = st.split()
print(tes)
print(tes[0])
print(tes[1])
print(tes[2])
print(tes[-1])

print(tes[0:2])

print(tes[:: -1])

print("--------------------------")

s1 = ' test1 test2 test3 '

s2 = s1[:: -1]

print(s2)

print(id(s1))
print(id(s2))

print("--------------------------")


arlis = [['a', 'b', 'c'], [4, 5, 6], [7, 8, 9]]

print(arlis[0][2])

print('--------------------------')

boys = ['Tom', 'Bob', 'Sam']
girls = ['Ann', 'Liz', 'Sue']

pupils = boys + girls

pupils.append('Tim')

print(pupils)