import abc
class Video(abc.ABC):
    pass

class Romance(Video):
    def __init__(self, videoName, status, startTime):
        self.videoName = videoName
        self.price = 2 # undetermined
        self.status = status
        self.startTime = startTime
    
class NewRelease(Video):
    def __init__(self, videoName, status, startTime):
        self.videoName = videoName
        self.price = 5 # undetermined
        self.status = status
        self.startTime = startTime

class Comedy(Video):
    def __init__(self, videoName, status, startTime):
        self.videoName = videoName
        self.price = 2 # undetermined
        self.status = status
        self.startTime = startTime
    
class Horror(Video):
    def __init__(self, videoName, status, startTime):
        self.videoName = videoName
        self.price = 4 # undetermined
        self.status = status
        self.startTime = startTime

class Drama(Video):
    def __init__(self, videoName, status, startTime):
        self.videoName = videoName
        self.price = 3 # undetermined
        self.status = status
        self.startTime = startTime

videoList = []
for _ in range(1, 6):
    locals()['Romance'+str(_) ] = Romance(f'Romance{_}', 'Onboard', None)
    videoList.append(f'Romance{_}')
for _ in range(1, 6):
    locals()['NewRelease'+str(_) ] = NewRelease(f'NewRelease{_}', 'Onboard', None)
    videoList.append(f'NewRelease{_}')
for _ in range(1, 6):
    locals()['Comedy'+str(_) ] = Comedy(f'Comedy{_}', 'Onboard', None)
    videoList.append(f'Comedy{_}')
for _ in range(1, 6):
    locals()['Horror'+str(_) ] = Romance(f'Horror{_}', 'Onboard', None)
    videoList.append(f'Horror{_}')
for _ in range(1, 6):
    locals()['Drama'+str(_) ] = Romance(f'Drama{_}', 'Onboard', None)
    videoList.append(f'Drama{_}')

print(videoList)
