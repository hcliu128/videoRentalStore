import person
import video

class Store():
    def __init__(self):
        self.videoStatus = ['Onboard' for i in range(20)]
        self.customerList = person.Customer_list
        self.videoInventory = 20
        self.dailyRecord = []

    def lendVideo(self, **kwargs):
        (person, video, startTime) = (kwargs['person'], kwargs['video'], kwargs['startTime'])
        video.status = person.Name
        video.startTime = startTime
        person.Video_Count += 1

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

    

# if __name__ == "__main__":
store = Store()
# dailyRecord 寫法？
store.lendVideo(video = video.Romance1, person = person.Customer_list[0], startTime = 1)
print(person.Customer_list[0].Video_Count)
print(video.Romance1.status)
store.returnVideo(video = video.Romance1, person = person.Customer_list[0], endTime = 3, price = video.Romance1.price)
print(person.Customer_list[0].Video_Count)
print(video.Romance1.status)


        
