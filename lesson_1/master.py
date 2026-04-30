import classes


House1 = classes.House("Georgia", 20)   
House2 = classes.House("Germany", 30)

print(House1.address + " " + str(House1.number))
print(House2.number)

House1.bulid()
House2.bulid()