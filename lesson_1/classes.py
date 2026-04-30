class House():
    """
    House class
    """
    def __init__(self,  address, number):
        self.number = number
        self.address = address
        self.age = 0


    def bulid(self):
        print("Building a house " + self.address + " " + str(self.number))    


class Prospect(House):
    def __init__(self, prospect,number):
        super().__init__(self,number)
        self.prospect = prospect

ProspectHouse = Prospect("Georgia", 20)        

print(ProspectHouse.prospect)