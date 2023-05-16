import random
import videostore
class Person:
    def __init__(self, name, video_count, character):
        self.name = name
        self.video_count = video_count
        self.character = character
        self.data = {}

    def Rentvideo(self,**kwargs):
        (person, video, start_time, onboard, videostore) = (kwargs['person'], kwargs['video'], kwargs['start_time'], kwargs['onboard'], kwargs['videostore'])
        if video.status == 'Onboard' and self.video_count < 3:
            video.status = self.name
            video.start_time = start_time
            person.video_count += 1
            if self.character == 'Breezy':
                video.duration = random.randint(1,2)
            elif self.character == 'Hoarders':
                video.duration = 7
            elif self.character == 'Regular':
                video.duration = random.randint(3, 5)
            else:
                print('error')
            videostore.video_inventory -= 1
            print('|success lend','|video=' + video.video_name,'\t|status=' + video.status,'\t|start time=' + str(video.start_time),'|count=' + str(self.video_count))

    def ReturnVideo(self,**kwargs):
        (person, video, price) = (kwargs['person'], kwargs['video'], kwargs['price'])
        video.status = 'Onboard'
        start_time = video.start_time
        duration = video.duration
        if start_time + duration > 35:
            duration = 35 - start_time
            #print(f'change duration to {duration}')
        person.video_count -= 1
        self.data['person'] = self.name
        self.data['video'] = video.video_name
        self.data['rental_day'] = video.duration
        self.data['cost'] = duration * price
        print('|success return','|video='+video.video_name,'\t|status='+video.status,'\t|duration'+str(video.duration),'|count='+str(person.video_count),'|cost='+str(duration * price))
        video.start_time = 0
        video.duration = 0
    