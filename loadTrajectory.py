# Examples 01
# From https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm
#  Last version

import _thread
from cProfile import label
from concurrent.futures import process
import time
import os
from unicodedata import decimal
from urllib import response
from xml.etree.ElementTree import ProcessingInstruction
import numpy as np
import matplotlib.pyplot as loadTrajectory
import math

basis = 20
amplitudes = 9
Fs = 100
dt = 1/Fs   # Период времени
Fc = 20
sample = 100
t = np.arange(sample)
#loadImpact = np.arange(sample)
loadImpact = np.arange(0.0,100.0,1.0)

quer = basis + np.sin(2 * np.pi * Fc * t / Fs) * amplitudes

# Internal cycles = intCount
def runAmplitude(threadName, amplitude):
   intCount = 0
   while intCount < amplitude:
      os.system("ping -c1 192.168.1.1 > /dev/null 2>&1")
#      os.system("ping -c1 192.168.222.19 > /dev/null 2>&1")
#     For web server
#      os.system("curl curl 192.168.222.19:9000 > /dev/null 2>&1")
      intCount += 1
#     For diagnose only
#      print("amplitude = %s" % (intCount))
#      print ("%s, %s: %s" % (threadName, intCount, time.ctime(time.time()) ))

try:
    # External cycles = extCount
# !!   print ("begin: -- %s --" % (time.ctime(time.time()) ))
   for extCount in range(sample):
      loadImpact[extCount] = 0.0
      startTime = time.time_ns()
      _thread.start_new_thread(runAmplitude, (extCount, int(quer[extCount]), ) )
      endTime = time.time_ns()
      newRT = (endTime - startTime)/1000000.0
#      newLI = math.log10(newRT/newPT)*10.0
#!!!  If PT = 0.1 and coef = 10, we use:
#      newLI = math.log10(newRT)
#      loadImpact[extCount] = math.log10(newRT) * 1.0
      loadImpact[extCount] = newRT
#      newLI = math.log10(newRT/0.1)*10.0
#      loadImpact[extCount] = newLI
#     For diagnose only
#      print("%s, %s, %s" % (newRT, newPT, newLI))
      print("%s, %s, %s" % (newRT, 0.1, loadImpact[extCount]))

      time.sleep(0.1)
#     For diagnose only
#      os.system("curl 192.168.222.19:9000 > /dev/null 2>&1")
      #os.system("echo curl")

except:
   print("Error run generator")

# Build a graph
# !!print ("end: == %s ==" % (time.ctime(time.time()) ))
loadTrajectory.figure()
loadTrajectory.subplot(2,1,1)
loadTrajectory.plot(quer,label='Queries')
loadTrajectory.title('Load Trajectory')
loadTrajectory.xlabel('Time (in msec)')
loadTrajectory.ylabel('Amplitude (in queries)')
loadTrajectory.legend(loc='best')

loadTrajectory.subplot(2,1,2)
loadTrajectory.plot(t,loadImpact,'b-',label='RT')
#loadTrajectory.plot(0.1,'r-',label='RT')
loadTrajectory.legend(loc='best')
loadTrajectory.show()

# Wait for End process
#time.sleep(13)
while 0:
   pass
