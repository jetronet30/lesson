# read write failes
import os
from pathlib import Path

# file = Path("test.txt")
# file.touch()

# file=open("test.txt", "+w")
# file.write("hello world")
# file.close


# file = open("test_2.txt", "+w")
# file.write("hello world 1213\n")
# print(file.read())
# print(file.closed)
# file.close

# file = open("test_2.txt", "r")
# print(file.read())
# file.close

with open("example.txt", "+w") as file:
    print("hello world", file=file, end="")
    # print(file.read())
    print(file.closed)

with open("example_1.txt", "wt") as file:
    n = file.write("python hello world")
    print(file.closed)
print(n)


s = [i for i in range(10)]
with open("example_2.txt", "wt") as file:
    for i in s:
        file.write(str(i) + " ")


with open("example_2.txt", "rt") as file:
    print(file.read())


print("------------------")


with open("example_2.txt") as file:
    # print(file.read(5))
    # print(file.readline())
    # print(file.readline())
    print(file.readlines())


print("------------------")

with open("example_3_ge.txt", "wt", encoding="utf-8") as file:
    file.write("სდჯკფდლსკფ სჯდფ;დკდ სდკსკდ")

with open("example_3_ge.txt", encoding="utf-8") as file:
    for line in file:
        print(line)



with open("example_3_ge.txt", encoding="utf-8") as file:
    print(file.read(2))  
    print(file.tell())    
    file.seek(6)
    print(file.tell())
    print(file.read())
