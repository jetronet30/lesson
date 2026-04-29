def out():
    a = 10
    b = 5
    def closure():
        return a + b
    return closure       # ფრჩხილების გარეშე  



print(out()())


print("------------------")

def my_func_2(x):
    def my_func_1():
        return x[1] + x[2]
    return my_func_1

sp = [1, 2, 3, 4, 5]
termit = my_func_2(sp)


print(termit())

sp[1] = 100
print(termit())


print("------------------")

# decorators

def my_decorator(func):
    def wrapper():
        print("start wrapper")
        func()
        print("stop wrapper")
    return wrapper

def main_func():
    print("start main func")
    print("stop main func")

my = my_decorator(main_func)
print(my)
my()

print("------------------")

@my_decorator
def main_func_2():
    print("start main func")
    print("stop main func")

main_func_2()


print("------------------")

def my_decorator_1(func):
    def wrapper(b):
        print("start wrapper")
        func(b)
        print("stop wrapper")
    return wrapper

@my_decorator_1
def main_func_3(a):
    return print(a * a)

main_func_3(12)


print("------------------")

def my_decorator_2(func):
    def wrapper():
        new = func().upper() + "!"
        return new
    return wrapper

def my_decorator_3(func):
    def wrapper():
        new = func() + "?"
        return new
    return wrapper

@my_decorator_2
@my_decorator_3
def main_func_4():
    return "hello"

print(main_func_4())