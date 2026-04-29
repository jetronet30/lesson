def my_func_1():
    print("start my func")
    def inner_func():
        print("start inner func")
        print("stop inner func")
    inner_func()
    print("stop my func")


my_func_1() 


print("------------------")



def my_func_2(n):

    print("start my func")
    def inner_func():
       pr = 1
       for i in range(1, n):
           pr *= i
       print(pr)
       return pr
    if n > 15:
        return inner_func()
    else:
        print("stop my func")
    
print("stop my func")



my_func_2(20)


print("------------------")

# non local variable

b =10 

def func_4():
    b=111
    print(b)
    def inner_func():
        nonlocal b    # nonlocal 
        b = 222
        print(b)
    inner_func()
    print(b)


print(b)
func_4()  
print(b)  


print("------------------")

def func_5():
    b=111
    print(b)
    def inner_func():
        global b    # global
        b = 222
        print(b)
    inner_func()
    print(b)

print(b)
func_5()  
print(b)

