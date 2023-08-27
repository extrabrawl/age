class user:
    name = ""
    lastname = ""
    age = 0
    mail = ""
    def printname(self):
        print(self.name, self.lastname)
    def checkage(self):
        if self.age >= 18:
            print("Вы совершеннолетний")
        elif self.age != 0:
            print("Вы не совершеннолетний")
        else:
            print("Вы не задали возраст")
    def setage(self, age):
        self.age = age
    def getage(self):
        return self.age  

user1 = user()
user2 = user()
user2.name = "Vasya"
user2.setage(26)
user1.setage(25)
user1.lastname = "Eremeev"
user1.name = "Ivan"
user1.printname()
print(user1.getage())
