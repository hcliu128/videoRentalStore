class VideoStore:
    def __init__(self):
        self.videos = [[0 for j in range(4)] for i in range(5)]
        self.dailyRecord = []
        self.Customer_list = []
        self.videoInventory = 20
    def add_video(self,video):
        self.videos = video
    def add_customer(self):
        pass
    def show_video(self):
        #print(self.videos)
        for i in range(5):
            for j in range(4):
                print(self.videos[i][j].videoName,self.videos[i][j].status,self.videos[i][j].startTime)
    def lend(self):
        pass
    def Return(self):
        pass
    def Daily_record(self):
        pass        