import abc
class Video(abc.ABC):
    pass

class Romance(Video):
    def __init__(self, videoName, price, status, startTime):
        self.videoName = videoName
        self.price = 2 # undetermined
        self.status = status
        self.startTime = startTime
    
class NewRelease(Video):
    def __init__(self, videoName, price, status, startTime):
        self.videoName = videoName
        self.price = 5 # undetermined
        self.status = status
        self.startTime = startTime

class Comedy(Video):
    def __init__(self, videoName, price, status, startTime):
        self.videoName = videoName
        self.price = 2 # undetermined
        self.status = status
        self.startTime = startTime
    
class Horror(Video):
    def __init__(self, videoName, price, status, startTime):
        self.videoName = videoName
        self.price = 4 # undetermined
        self.status = status
        self.startTime = startTime
    
a = Horror('1',  4, 'Home', '0512')
print(a.videoName)