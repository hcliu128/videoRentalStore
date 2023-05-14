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
    def __init__(self, videoName, status, startTime,endTime):
        self.videoName = videoName
        self.price = 4 # undetermined
        self.status = status
        self.startTime = startTime
        self.endTime = endTime