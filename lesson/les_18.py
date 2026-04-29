def func(x1, x2):
    c = x1 + x2
    d = x1 - x2
    return c, d

print(func(1, 2))
print(type(func(1, 2)))

a = 1000

def func(x1, x2):
    global a
    a = 100
    c = x1 + x2
    d = x1 - x2
    return c, d


print(a)
print(func(1, 2))
print(a)



print("------------------")

def func():
    l[1] = 1000
    return l


l = [1, 2, 3]
print(l)
print(func())
print(l)

print("------------------")

def func_43():
    global d
    d = 100
    b = 29
    print(locals() ,'\n', globals())

   
mn = [1, 2, 3]
func_43()

