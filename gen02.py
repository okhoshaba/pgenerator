# Examples 01
# From https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm

import _thread
import time
import os
import numpy as np
import matplotlib.pyplot as plt

basis = 20
amplitudes = 10
Fs = 500
f = 5
sample = 200
t = np.arange(sample)
quer = basis + np.sin(2 * np.pi * f * t / Fs) * amplitudes

    # Internal cycles = intCount
def runAmplitude(threadName, amplitude):
   intCount = 0
   while intCount < amplitude:
      intCount += 1
      print ("%s, %s: %s" % (threadName, intCount, time.ctime(time.time()) ))

try:
    # External cycles = extCount
   for extCount in range(sample):
       _thread.start_new_thread(runAmplitude, (extCount, int(quer[extCount]), ) )
       os.system("echo curl")
#       os.system("curl 192.168.222.19:9000 > /dev/null 2>&1")
       time.sleep(0.1)

except:
   print("Error run generator")

# Wait for End process
time.sleep(13)
while 0:
   pass
