import abc
class Video(abc.ABC):
    pass

class Romance(Video):
    def __init__(self, videoName, status, startTime, endTime):
        self.videoName = videoName
        self.price = 2 # undetermined
        self.status = status
        self.startTime = startTime
        self.endTime = endTime
    
class NewRelease(Video):
    def __init__(self, videoName, status, startTime, endTime):
        self.videoName = videoName
        self.price = 5 # undetermined
        self.status = status
        self.startTime = startTime
        self.endTime = endTime

class Comedy(Video):
    def __init__(self, videoName, status, startTime, endTime):
        self.videoName = videoName
        self.price = 2 # undetermined
        self.status = status
        self.startTime = startTime
        self.endTime = endTime
    
class Horror(Video):
    def __init__(self, videoName, status, startTime, endTime):
        self.videoName = videoName
        self.price = 4 # undetermined
        self.status = status
        self.startTime = startTime
        self.endTime = endTime

class Drama(Video):
    def __init__(self, videoName, status, startTime, endTime):
        self.videoName = videoName
        self.price = 3 # undetermined
        self.status = status
        self.startTime = startTime
        self.endTime = endTime
# 裝 video instance 的 list
videoList = []

for _ in range(1, 6):
    locals()['Romance'+str(_) ] = Romance(f'Romance{_}', 'Onboard', None, None)
    videoList.append(locals()['Romance'+str(_) ])
for _ in range(1, 6):
    locals()['NewRelease'+str(_) ] = NewRelease(f'NewRelease{_}', 'Onboard', None, None)
    videoList.append(locals()['NewRelease'+str(_) ])
for _ in range(1, 6):
    locals()['Comedy'+str(_) ] = Comedy(f'Comedy{_}', 'Onboard', None, None)
    videoList.append(locals()['Comedy'+str(_) ])
for _ in range(1, 6):
    locals()['Horror'+str(_) ] = Horror(f'Horror{_}', 'Onboard', None, None)
    videoList.append(locals()['Horror'+str(_) ])
for _ in range(1, 6):
    locals()['Drama'+str(_) ] = Drama(f'Drama{_}', 'Onboard', None, None)
    videoList.append(locals()['Drama'+str(_) ])

