import abc
class Video(abc.ABC):
    pass

class Romance(Video):
    def __init__(self, video_name, status, start_time, duration):
        self.video_name = video_name
        self.price = 2 
        self.status = status
        self.start_time = start_time
        self.duration = duration
    
class NewRelease(Video):
    def __init__(self, video_name, status, start_time, duration):
        self.video_name = video_name
        self.price = 5 
        self.status = status
        self.start_time = start_time
        self.duration = duration

class Comedy(Video):
    def __init__(self, video_name, status, start_time, duration):
        self.video_name = video_name
        self.price = 2 
        self.status = status
        self.start_time = start_time
        self.duration = duration
    
class Horror(Video):
    def __init__(self, video_name, status, start_time, duration):
        self.video_name = video_name
        self.price = 4 
        self.status = status
        self.start_time = start_time
        self.duration = duration
class Drama(Video):
    def __init__(self, video_name, status, start_time,duration):
        self.video_name = video_name
        self.price = 4 
        self.status = status
        self.start_time = start_time
        self.duration = duration