# a = int(input("enter num : "))


# number = a if a > 20 else 10000
# print(number)


print("1 ----- is fantastic")
print("2 ----- is batle")
print("3 ----- is tester")
print("4 ----- is horror")
print("5 ----- is comedy")

ganre = int(input("enter ganre : "))

match ganre:
    case 1:
        print("1 ----- is fantastic")
    case 2:
        print("2 ----- is batle")
    case 3:
        print("3 ----- is tester")
    case 4 | 5:
        print("4 ----- is horror")
        print("5 ----- is comedy")
    case _:
        print("error")
