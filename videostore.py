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
                print(self.videos_list[i][j].videoName,self.videos_list[i][j].status,self.videos_list[i][j].startTime,self.videos_list[i][j].endTime)
    def lendVideo(self, **kwargs):
        (person, video, startTime) = (kwargs['person'], kwargs['video'], kwargs['startTime'])
        video.status = person.Name
        video.startTime = startTime
        person.Video_Count += 1
        print('|success lend','|video='+video.videoName,'\t|status='+video.status,'\t|start time='+str(video.startTime),'|count='+str(person.Video_Count))
    def returnVideo(self, **kwargs):
        data = {}
        (person, video, endTime, price) = (kwargs['person'], kwargs['video'], kwargs['endTime'], kwargs['price'])
        video.status = 'Onboard'
        startTime = video.startTime
        video.endTime = endTime
        person.Video_Count -= 1
        data['person'] = person.Name
        data['video'] = video.videoName
        data['rental_day'] = endTime-startTime
        data['cost'] = (endTime-startTime) * price
        self.dailyRecord.append(data)
        print(data)
    def Daily_record(self):
        pass        