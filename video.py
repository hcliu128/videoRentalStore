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
    
a = Horror('1', 'Home', '0512')
print(a.videoName)

videoList = []
videoKind = ['Romance', 'NewRelease', 'Comedy', 'Horror']
for i in videoKind:
    for _ in range(1, 6):
        locals()[i+str(_) ] = Romance(f'{i}{_}', 'Onboard', None)
        videoList.append(f'{i}{_}')

print(videoList)
