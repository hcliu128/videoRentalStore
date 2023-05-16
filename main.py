import person
import video
import videostore
import random
class Main:
    def __init__(self):
        self.name_list = ['Emma','Liam','Olivia','Noah','Ava','Sophia','Jackson','Isabella','Aiden','Mia']
        self.character_list = ['Breezy','Hoarders','Regular']
        self.customer_list = [0 for i in range(10)]
        self.video = [[0 for j in range(4)] for i in range(5)]
        self.Romance_video = ['The Notebook','Titanic','Love Actually','La La Land']
        self.Comedy_video = ['Bridesmaids','The Hangover','Superbad','Anchorman']
        self.Horror_video = ['The Exorcist','The shining','Get Out','The Conjuring']
        self.Drama_video = ['The Shawshank Redemption','Forrest Gump','The Godfather','A star is Born']
        self.New_release_video = ['BlackBerry','Hypnotic','The Mother','Mercy']
        self.store = videostore.VideoStore()
    def set_customer(self):
        for i in range(10):
            rd = random.randint(0, 2)
            self.customer_list[i] =person.Person(self.name_list[i],0,self.character_list[rd])
            self.store.add_customer(self.customer_list)
    def show_customer(self):
        self.store.show_customer()
    def set_videos(self):
        for i in range(5):
            for j in range(4):
                if i==0:
                    self.video[i][j]=video.Romance(self.Romance_video[j], 'Onboard', 0,0)
                if i==1:
                    self.video[i][j]=video.Comedy(self.Comedy_video[j], 'Onboard', 0,0)
                if i==2:
                    self.video[i][j]=video.Horror(self.Horror_video[j], 'Onboard', 0,0)
                if i==3:
                    self.video[i][j]=video.Drama(self.Drama_video[j], 'Onboard', 0,0)
                if i==4:
                    self.video[i][j]=video.NewRelease(self.New_release_video[j], 'Onboard', 0,0)
        self.store.add_video(self.video)
    def show_video(self):
        self.store.show_video()
    def run(self,day):
        print(f'----------------Day{day} start-------------')
        if i>1:
            self.store.check_return(day)
        if day!=35:
            times = random.randint(0, int(self.store.video_inventory*0.4))
            for time in range(times):
                n = random.randint(0,9)
                video_type = random.randint(0,4)
                video_slot = random.randint(0,3)
                self.store.customer_list[n].Rentvideo(videostore=self.store,person = self.store.customer_list[n], video = self.store.videos_list[video_type][video_slot], start_time = day, onboard = self.store.video_inventory)
        self.store.video_in_shop(day)
        if day==35:
            self.store.show_income()
main = Main()
main.set_customer()
main.set_videos()
for i in range(1,36):
    main.run(i)

