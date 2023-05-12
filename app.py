import random
class Person:
    def __init__(self,Name,Video_Count,Character):
        self.Name = Name
        self.Video_Count = Video_Count
        self.Character = Character
    def Rent():
        pass
    def Return():
        pass

# create customer
Name_list = ['Emma','Liam','Olivia','Noah','Ava','Sophia','Jackson','Isabella','Aiden','Mia']
Character_list = ['Breezy','Hoarders','Regular']
Customer_list = [0 for i in range(10)]
for i in range(10):
    rd = random.randint(0, 2)
    Customer_list[i] =Person(Name_list[i],0,Character_list[rd])
    print(Customer_list[i].Name,Customer_list[i].Video_Count,Customer_list[i].Character)


