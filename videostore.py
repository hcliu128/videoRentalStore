class VideoStore:
    def __init__(self):
        self.videos_list = [[0 for j in range(4)] for i in range(5)]
        self.customer_list =[]
        self.video_inventory = 20
        self.__video_in_shop = []
        self.__income = 0
    
    def add_video(self,video):
        self.videos_list = video
    
    def add_customer(self,Person):
        self.customer_list = Person
    
    def show_customer(self):
        for i in range(10):
            print(self.customer_list[i].name, self.customer_list[i].video_count, self.customer_list[i].character)
    
    def show_video(self):
        for i in range(5):
            for j in range(4):
                print(self.videos_list[i][j].video_name, self.videos_list[i][j].status, self.videos_list[i][j].startTime, self.videos_list[i][j].duration)
    
    def total_count(self,money):
        self.__income += money
    def show_income(self):
        print('total income :',self.__income)
    def check_return(self,day):
        for i in range(5):
            for j in range(4):
                if self.videos_list[i][j].duration + self.videos_list[i][j].start_time == day:
                    for k in range(len(self.customer_list)):
                        if self.videos_list[i][j].status == self.customer_list[k].name:
                            self.customer_list[k].ReturnVideo(video = self.videos_list[i][j], person = self.customer_list[k], price = self.videos_list[i][j].price)
                            self.video_inventory+=1
                            self.total_count(self.customer_list[k].data['cost']) 
                            break
                if day==35:
                    for i in range(5):
                        for j in range(4):
                            if self.videos_list[i][j].duration != 0:
                                for k in range(len(self.customer_list)):
                                    if self.videos_list[i][j].status == self.customer_list[k].name:
                                        self.customer_list[k].ReturnVideo(video=self.videos_list[i][j],person=self.customer_list[k],price = self.videos_list[i][j].price)
                                        self.video_inventory += 1
                                        break
        
    def video_in_shop(self,day):
        toady =[]
        for i in range(5):
            for j in range(4):
                if self.videos_list[i][j].status =='Onboard':
                    toady.append(self.videos_list[i][j].video_name)
        self.__video_in_shop.append(toady)
        print(len(self.__video_in_shop[day-1]),'videos in shop:',self.__video_in_shop[day-1])



        