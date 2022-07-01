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

basis = 1000
amplitudes = 500
#basis = 200
#amplitudes = 50
Fs = 100
#dt = 1/Fs   # Период времени
Fc = 20
sample = 100
t = np.arange(sample)
loadImpact = np.arange(0.0,100.0,1.0)
RT = np.arange(0.0,100.0,1.0)
bnx = (1,50,100)
bny = (0,0,0)

quer = basis + np.sin(2 * np.pi * Fc * t / Fs) * amplitudes

# Internal cycles = intCount
def runAmplitude(threadName, amplitude):
   intCount = 0
   while intCount < amplitude:
      os.system("curl 192.168.1.108:9000 > /dev/null 2>&1")
#      os.system("ping -c1 192.168.1.1 > /dev/null 2>&1")
#      os.system("ping -c1 192.168.222.19 > /dev/null 2>&1")
#     For web server
#      os.system("curl 192.168.222.19:9000 > /dev/null 2>&1")
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
# in ms      
      RT[extCount] = (endTime - startTime)
#      RT = (endTime - startTime)/1000000
#      newLI = math.log10(newRT/newPT)*10.0
#!!!  If PT = 0.1 and coef = 10, we use:
#      newLI = math.log10(newRT)
#      loadImpact[extCount] = math.log10(newRT) * 1.0
      loadImpact[extCount] = math.log10(1000000/RT[extCount])
#      newLI = math.log10(newRT/0.1)*10.0
#      loadImpact[extCount] = newLI
#     For diagnose only
#      print("%s, %s, %s" % (newRT, newPT, newLI))
      print("%s, %s, %s" % (RT[extCount], quer[extCount], loadImpact[extCount]))

      time.sleep(0.001)
#     For diagnose only
#      os.system("curl 192.168.222.19:9000 > /dev/null 2>&1")
      #os.system("echo curl")

except:
   print("Error run generator")

# Build a graph
# !!print ("end: == %s ==" % (time.ctime(time.time()) ))
loadTrajectory.figure()
loadTrajectory.subplot(3,1,1)
loadTrajectory.plot(quer,label='Queries')
loadTrajectory.title('Load Trajectory')
#loadTrajectory.xlabel('Samples')
loadTrajectory.ylabel('Amplitude (in queries)')
loadTrajectory.legend(loc='best')

loadTrajectory.subplot(3,1,2)
#loadTrajectory.title('Response Time (RT)')
#loadTrajectory.xlabel('Samples')
loadTrajectory.ylabel('Response Time (in 1e-3 sec.)')
loadTrajectory.plot(t,RT,'b-',label='RT')
loadTrajectory.legend(loc='best')

loadTrajectory.subplot(3,1,3)
#loadTrajectory.title('Load Impact')
loadTrajectory.xlabel('Samples')
loadTrajectory.ylabel('Load Impact (in #)')
loadTrajectory.plot(t,loadImpact,'b-',label='loadImpact')
loadTrajectory.plot(bnx, bny, 'r-', label='Bottleneck')
#loadTrajectory.plot(0.1,'r-',label='RT')
loadTrajectory.legend(loc='best')

loadTrajectory.show()

# Wait for End process
#time.sleep(13)
while 0:
   pass
