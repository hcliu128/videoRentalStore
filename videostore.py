class VideoStore:
    def __init__(self):
        self.videos_list = [[0 for j in range(4)] for i in range(5)]
        self.dailyRecord = []
        self.Customer_list =[]
        self.videoInventory = 20
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
    def Daily_record(self,data):
        self.dailyRecord.append(data)
    def check_return(self,day):
        for i in range(5):
            for j in range(4):
                if self.videos_list[i][j].duration + self.videos_list[i][j].startTime ==day:
                    for k in range(len(self.Customer_list)):
                        #print(self.videos_list[i][j].status,self.Customer_list[k].Name)
                        if self.videos_list[i][j].status == self.Customer_list[k].Name:
                            self.Customer_list[k].ReturnVideo(video = self.videos_list[i][j], person = self.Customer_list[k], price = self.videos_list[i][j].price)
                            self.videoInventory+=1
                            print(f'resting{self.videoInventory}')
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
                                        print(f'resting {self.videoInventory}')
                                        break