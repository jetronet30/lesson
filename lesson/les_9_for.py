s = 'hello'

for i in s:
    print(i)
print('------------------')

for i in 23, 45, 67, 'python', [1, 2, 3]: 
    print(i)   

print('------------------')   
for i in range(5):
    print(i) 

print('------------------')
for i in range(2, 12, 2):
    print(i)   

print('------------------')
for i in range(10, 0, -2):
    if i == 4:
        print('break')
        break
    print(i)     


print('------------------')
print('continue')
for i in range(1, 10):
    for j in range(1, 10):
        print(i, '*', j, '=', i * j, end=' | ')
    print()

print('------------------')
for i in enumerate(s, 4):
    print(i)



print('------------------')
for i in s:
    if i == 'l':
        print('continue')
        continue
    print(i) 