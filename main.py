import person
import video
import videostore
import random
import datetime
class Main:
    def __init__(self):
        self.Name_list = ['Emma','Liam','Olivia','Noah','Ava','Sophia','Jackson','Isabella','Aiden','Mia']
        self.Character_list = ['Breezy','Hoarders','Regular']
        self.Customer_list = [0 for i in range(10)]
        self.Video = [[0 for j in range(4)] for i in range(5)]
        self.Romance_video = ['The Notebook','Titanic','Love Actually','La La Land']
        self.Comedy_video = ['Bridesmaids','The Hangover','Superbad','Anchorman']
        self.Horror_video = ['The Exorcist','The shining','Get Out','The Conjuring']
        self.Drama_video = ['The Shawshank Redemption','Forrest Gump','The Godfather','A star is Born']
        self.New_release_video = ['BlackBerry','Hypnotic','The Mother','Mercy']
        self.store = videostore.VideoStore()
        self.onboard = 20
    def set_customer(self):
        for i in range(10):
            rd = random.randint(0, 2)
            self.Customer_list[i] =person.Person(self.Name_list[i],0,self.Character_list[rd])
            self.store.add_customer(self.Customer_list)
    def show_customer(self):
        self.store.show_customer()
    def set_videos(self):
        for i in range(5):
            for j in range(4):
                if i==0:
                    self.Video[i][j]=video.Romance(self.Romance_video[j], 'Onboard', 0, 0)
                if i==1:
                    self.Video[i][j]=video.Comedy(self.Comedy_video[j], 'Onboard', 0, 0)
                if i==2:
                    self.Video[i][j]=video.Horror(self.Horror_video[j], 'Onboard', 0, 0)
                if i==3:
                    self.Video[i][j]=video.Drama(self.Drama_video[j], 'Onboard', 0, 0)
                if i==4:
                    self.Video[i][j]=video.NewRelease(self.New_release_video[j], 'Onboard', 0, 0)
        self.store.add_video(self.Video)
    def show_video(self):
        self.store.show_video()
    def run(self,day):
        print(f'----------Day{day} start----------') 
        if i > 1:self.check_return(day) #在一天的開始先確定有沒有人租約到期
        if day != 35: #若不是最後一天才可以租
            times = random.randint(0, int(self.onboard * 0.4)) #0.4只是符合一般性假設 怕開店第一天就沒片子
            for time in range(times):
                n = random.randint(0,9)
                video_type = random.randint(0,4)
                video_slot = random.randint(0,3)
                self.onboard = videostore.VideoStore.lendVideo(person = self.store.Customer_list[n],video = self.store.videos_list[video_type][video_slot],startTime = day, onboard = self.onboard)
                
                
                # self.store.returnVideo(video = self.store.videos_list[video_type][video_slot], person = self.store.Customer_list[n], endTime = day+3, price = self.store.videos_list[video_type][video_slot].price)
            print(f'----------Day{day} end----------')
    def check_return(self, day):
        for i in range(5):
            for j in range(4):
                if self.Video[i][j].duration + self.Video[i][j].startTime == day :
                    self.store.returnVideo(video = self.store.videos_list[i][j], person = self.store.videos_list[i][j].status, price = self.store.videos_list[i][j].price)
                    self.onboard += 1
                    print(f'resting {self.onboard}')
        if day == 35 : #35天 直接強迫還
            for i in range(5):
                for j in range(4):
                    if self.store.videos_list[i][j].duration != 0:
                        self.store.returnVideo(video = self.store.videos_list[i][j], person = self.store.videos_list[i][j].status, price = self.store.videos_list[i][j].price)
                        self.onboard += 1
                        print(f'resting {self.onboard}')


main = Main()
main.set_customer()
#main.show_customer()
main.set_videos()
#main.show_video()
for i in range(1, 36):
    main.run(i)

