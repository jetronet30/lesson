import time


def fun_1():
    print("start")
    time.sleep(2)
    print("stop")


def fun_2():
    print("start_2")
    time.sleep(2)
    print("stop_2")
    return True


def fun_3(a, b):
    print("start_3")
    time.sleep(2)
    print("stop_3")
    print(a, b)
    return a * b


def fun_4(a=10, b=20):
    print("start_4")
    time.sleep(2)
    print("stop_4")
    print(a, b)
    print(a * b)
    return a * b


fun_1()

print(fun_2())

print(fun_3(4, 5))

fun_3(a=4, b=5)

fun_4()

# n1 = int(input("Enter a number n1: "))
# n2 = int(input("Enter a number n2: "))

# print(fun_3(n1, n2))


print("------------------")

def fun_5(*args):
    return args  


print(fun_5(1, 2, 3, 4, 5, 'hello', 'world'))


def fun_6(**kwargs):
    return kwargs   

print(fun_6(a=1, b=2, c=3, d=4, e=5, f='hello', g='world'))


print("------------------")

def fun_7(*args, **kwargs):
    return args, kwargs


print(fun_7(1, 2, 3, 4, 5, 'hello', 'world', a=1, b=2, c=3, d=4, e=5, f='hello', g='world'))