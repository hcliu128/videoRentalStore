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
    def set_customer(self):
        for i in range(10):
            rd = random.randint(0, 2)
            self.Customer_list[i] =person.Person(self.Name_list[i],0,self.Character_list[rd])
    def show_customer(self):
        for i in range(10):
            print(self.Customer_list[i].Name,self.Customer_list[i].Video_Count,self.Customer_list[i].Character)
    def set_videos(self):
        for i in range(5):
            for j in range(4):
                if i==0:
                    self.Video[i][j]=video.Romance(self.Romance_video[j], True, datetime.date.today())
                if i==1:
                    self.Video[i][j]=video.Comedy(self.Comedy_video[j], True, datetime.date.today())
                if i==2:
                    self.Video[i][j]=video.Horror(self.Horror_video[j], True, datetime.date.today())
                if i==3:
                    self.Video[i][j]=video.Drama(self.Drama_video[j], True, datetime.date.today())
                if i==4:
                    self.Video[i][j]=video.NewRelease(self.New_release_video[j], True, datetime.date.today())
        self.store.add_video(self.Video)
    def show_video(self):
        self.store.show_video()
    def run():
        for i in range(34):
            pass

main = Main()
main.set_customer()
main.show_customer()
main.set_videos()
main.show_video()

