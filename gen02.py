# Examples 01
# From https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm

import _thread
import time
import os
import numpy as np
import matplotlib.pyplot as plt

    # Internal cycles = intCount
def runAmplitude(threadName, amplitude):
   intCount = 0
   while intCount < amplitude:
      intCount += 1
      print ("%s, %s: %s" % (threadName, intCount, time.ctime(time.time()) ))

try:
   basis = 20
   amplitudes = 10
   Fs = 500
   f = 5
   sample = 200
   t = np.arange(sample)
   quer = basis + np.sin(2 * np.pi * f * t / Fs) * amplitudes
    # External cycles = extCount
   for extCount in range(t):
       _thread.start_new_thread(runAmplitude, (extCount, quer[extCount], ) )
       os.system("echo curl")
#       os.system("curl 192.168.222.19:9000 > /dev/null 2>&1")
       time.sleep(0.1)

except:
   print("Error run generator")

# Wait for End process
time.sleep(13)
while 0:
   pass
