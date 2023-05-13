import person
import video

class Store():
    def __init__(self):
        self.videoStatus = ['Onboard' for i in range(20)]
        self.customerList = person.Customer_list
        self.videoInventory = 20
        self.dailyRecord = []


store = Store()
for i in range(10):
    print(store.customerList[i].Name)

        
