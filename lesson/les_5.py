# x = int(input("Enter a number: "))

# if x >= 0:
#     print("The number is positive.")
# elif x == 0:
#     print("The number is zero.")
# else:
#     print("The number is negative.")

# name = input("Enter your name: ")

# if name :
#     print("Hello, " + name + "!")
# else:    
#     print("No name entered.")
    

# a = True    
# b = False

# if a:
#     if b:
#         print("Both a and b are True.")
#     else:
#         print("a is True but b is False.")    
# else:
#     print("a is False.")        



# a = int(input("Enter a number: "))

# if 10 <= a <= 20:
#     print("The number is between 10 and 20.")
# else:
#     print("The number is outside the range of 10 to 20.")    

a = int(input("Enter a number: "))

if a == 10 or a == 20 or a == 30:
    print(10, 20, 30)
elif a > 10 and a < 100:
    print(10, 100)    
elif a != 10 and a != 20 and a != 30:
    print("The number is less than 10 and not 10, 20, or 30.")    
else:
    print(a)    
