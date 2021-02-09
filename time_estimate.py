import time

class TimeEstimate:

    def __init__(self):
        """
        Once the object is created, the starting would be set up.
        """
        self.start_time = time.time()        
    
    def estimate(self, done_jobs: int, total_jobs: int) -> int:
        """
        return hours, minutes, seconds
        """
        if done_jobs == 0:
            return 0, 0, 0
        s = int(time.time() - self.start_time)
        s = (s / done_jobs) * (total_jobs - done_jobs)
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        return int(hours), int(minutes), int(seconds)


timer = TimeEstimate()
for i in range(1, 101):
    hour, minute, second = timer.estimate(i, 100)
    print(hour, minute, second)
    time.sleep(1)