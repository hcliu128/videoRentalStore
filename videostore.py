class VideoStore:
    def __init__(self):
        self.videos_list = [[0 for j in range(4)] for i in range(5)]
        self.dailyRecord = []
        self.Customer_list =[]
        self.videoInventory = 20
        self.__video_in_shop = []
        self.__income = 0
    
    def add_video(self,video):
        self.videos_list = video
    
    def add_customer(self,Person):
        self.Customer_list = Person
    
    def show_customer(self):
        for i in range(10):
            print(self.Customer_list[i].Name,self.Customer_list[i].Video_Count,self.Customer_list[i].Character)
    
    def show_video(self):
        #print(self.videos)
        for i in range(5):
            for j in range(4):
                print(self.videos_list[i][j].videoName,self.videos_list[i][j].status,self.videos_list[i][j].startTime,self.videos_list[i][j].duration)
    
    def total_count(self,money):
        self.__income+=money
    def show_income(self):
        print('total income',self.__income)
    def check_return(self,day):
        for i in range(5):
            for j in range(4):
                if self.videos_list[i][j].duration + self.videos_list[i][j].startTime ==day:
                    for k in range(len(self.Customer_list)):
                        #print(self.videos_list[i][j].status,self.Customer_list[k].Name)
                        if self.videos_list[i][j].status == self.Customer_list[k].Name:
                            self.Customer_list[k].ReturnVideo(video = self.videos_list[i][j], person = self.Customer_list[k], price = self.videos_list[i][j].price)
                            self.videoInventory+=1
                            self.total_count(self.Customer_list[k].data['cost']) 
                            #print(f'resting{self.videoInventory}')
                            break
                if day==35:
                    for i in range(5):
                        for j in range(4):
                            if self.videos_list[i][j].duration !=0:
                                for k in range(len(self.Customer_list)):
                                    if self.videos_list[i][j].status == self.Customer_list[k].Name:
                                        #index = self.Customer_list.index(self.videos_list[i][j].status)
                                        self.Customer_list[k].ReturnVideo(video=self.videos_list[i][j],person=self.Customer_list[k],price = self.videos_list[i][j].price)
                                        self.videoInventory+=1
                                        #print(f'resting {self.videoInventory}')
                                        break
        
    def video_in_shop(self,day):
        toady =[]
        for i in range(5):
            for j in range(4):
                if self.videos_list[i][j].status =='Onboard':
                    toady.append(self.videos_list[i][j].videoName)
        self.__video_in_shop.append(toady)
        print(len(self.__video_in_shop[day-1]),'videos in shop:',self.__video_in_shop[day-1])


        
