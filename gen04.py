# Examples 01
# From https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm

import _thread
from concurrent.futures import process
import time
import os
from urllib import response
from xml.etree.ElementTree import ProcessingInstruction
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as loadTrajectory
import scipy

basis = 20
amplitudes = 10
Fs = 500
f = 5
sample = 200
t = np.arange(sample)
responseTime = np.arange(sample)

quer = basis + np.sin(2 * np.pi * f * t / Fs) * amplitudes
processingTime = 0.1 / quer

# Internal cycles = intCount
def runAmplitude(threadName, amplitude):
   intCount = 0
   while intCount < amplitude:
      intCount += 1
#     For diagnose only
#      print("amplitude = %s" % (intCount))
#      print ("%s, %s: %s" % (threadName, intCount, time.ctime(time.time()) ))

try:
    # External cycles = extCount
   for extCount in range(sample):
      startTime = time.time_ns()
      _thread.start_new_thread(runAmplitude, (extCount, int(quer[extCount]), ) )
      endTime = time.time_ns()
#      os.system("curl 192.168.222.19:9000 > /dev/null 2>&1")
      os.system("echo curl")
      responseTime[extCount] = endTime - startTime
      time.sleep(0.1)
#     For diagnose only
#      os.system("echo curl")

except:
   print("Error run generator")

# Build a graph
# loadTrajectory.plot(quer)
# loadTrajectory.title('Load Trajectory')
# loadTrajectory.xlabel('Time (in sec)')
# loadTrajectory.ylabel('Amplitude (in queries)')
# loadTrajectory.show()

#plt.plot(processingTime)
# !! plt.plot(responseTime)
# !! plt.show()

plt.subplot(3,1,1)
plt.plot(responseTime)

plt.subplot(3,1,2)
plt.plot(processingTime)

plt.subplot(3,1,3)
plt.plot(responseTime/processingTime)

plt.show()


# Wait for End process
#time.sleep(13)
while 0:
   pass
