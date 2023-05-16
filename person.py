import random
import videostore
class Person:
    def __init__(self,Name,Video_Count,Character):
        self.Name = Name
        self.Video_Count = Video_Count
        self.Character = Character
    
    def Rentvideo(self,**kwargs):
        (person, video, startTime,onboard,videostore) = (kwargs['person'], kwargs['video'], kwargs['startTime'],kwargs['onboard'],kwargs['videostore'])
        if video.status == 'Onboard' and self.Video_Count<3:
            video.status = self.Name
            video.startTime = startTime
            person.Video_Count += 1
            print(self.Character)
            if self.Character == 'Breezy':
                video.duration = random.randint(1,2)
            elif self.Character == 'Hoarders':
                video.duration = 7
            elif self.Character == 'Regular':
                video.duartion = random.randint(3, 5)
            else:
                print('error')
            videostore.videoInventory-=1
            print('|success lend','|video='+video.videoName,'\t|status='+video.status,'\t|start time='+str(video.startTime),'\t|duration='+str(video.duration),'|count='+str(self.Video_Count))
            print(f'resting {videostore.videoInventory}')

    def ReturnVideo(self,**kwargs):
        data = {}
        (person, video, price) = (kwargs['person'], kwargs['video'], kwargs['price'])
        video.status = 'Onboard'
        startTime = video.startTime
        duration = video.duration
        if startTime + duration > 35:
            duration = 35 - startTime
            print(f'change duration to {duration}')
        person.Video_Count -= 1
        data['person'] = self.Name
        data['video'] = video.videoName
        data['rental_day'] = video.duration
        data['cost'] = duration * price
        #videostore.Daily_record(data)
        print(data)
        print('|success return','|video='+video.videoName,'\t|status='+video.status,'\t|duration'+str(video.duration),'|count='+str(person.Video_Count))
        video.startTime = 0
        video.duration = 0        

