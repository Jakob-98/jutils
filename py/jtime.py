import time

class Timer:
   def __init__(self, printupdates = False):
    self.starttime = time.time()
    self.deltatime = time.time()
    self.printupdates = printupdates

   def updatetime(self, updatemsg: str):
    if not self.printupdates: return
    prevtime = self.deltatime
    self.deltatime = time.time()
    print(updatemsg, '%.2f' % float(1000*(self.deltatime - prevtime)), 'ms')
   
   def totalTime(self, updatemsg: str):
    print(updatemsg, '%.2f' % float(1000*(time.time() - self.starttime)), 'ms')