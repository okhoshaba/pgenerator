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
import scipy.fftpack
import math

basis = 9
amplitudes = 3
Fs = 1000
dt = 1/Fs   # Период времени
Fc = 10
sample = 1000
t = np.arange(sample)
loadImpact = np.arange(sample)
responseTime = np.arange(sample)
#procTime = np.arange(sample)

quer = basis + np.sin(2 * np.pi * Fc * t / Fs) * amplitudes
processingTime = 0.1 / quer

# Internal cycles = intCount
def runAmplitude(threadName, amplitude):
   intCount = 0
   while intCount < amplitude:
      os.system("curl 192.168.1.104:9000 > /dev/null 2>&1")
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
      responseTime[extCount] = endTime - startTime
      rp = responseTime[extCount]/1000000
      loadImpact[extCount] = math.log10(0.1/rp) * 1000
#!!      print("%s, %s, %s, %s, %s, %s, %s" % (extCount, int(quer[extCount]), 0.1, responseTime[extCount]/1000000, 0.1/rp, math.log10(0.1/rp)*10, loadImpact[extCount]))
      time.sleep(0.1)
#      os.system("curl 192.168.222.19:9000 > /dev/null 2>&1")
      #os.system("echo curl")
#     For diagnose only
#      os.system("echo curl")

except:
   print("Error run generator")

# Build a graph
loadTrajectory.plot(quer)
loadTrajectory.title('Load Trajectory')
loadTrajectory.xlabel('Time (in msec)')
loadTrajectory.ylabel('Amplitude (in queries)')
loadTrajectory.show()

#   Fourier Analise
# ...
x2 = np.linspace(0.0, 1, Fs)
#y2 = amplitudes * np.sin(2 * np.pi * Fc * x2)
#yf2 = scipy.fftpack.fft(y2)
#yf2 = scipy.fftpack.fft(math.log10(responseTime/processingTime))
# !! yf2 = scipy.fftpack.fft(processingTime)
xf2 = np.linspace(0.0, 1.0/(2.0*dt), Fs//2)
yf2 = scipy.fftpack.fft(loadImpact)
ymax = max(2.0/Fs * np.abs(yf2[:Fs//2]))
print(ymax)

fig, ax = plt.subplots()

# Plotting only the left part of the spectrum to not show aliasing
#ax.plot(xf1, 2.0/N * np.abs(yf1[:N//2]), label='fftpack tutorial')
ax.plot(xf2, 2.0/Fs * np.abs(yf2[:Fs//2]), label='Integer number of periods')
#ax.plot(xf3, 2.0/N * np.abs(yf3[:N//2]), label='Correct positioning of dates')
plt.legend()
plt.grid()
plt.show()

#print(yf2[:Fs//2])

#plt.plot(processingTime)
#  plt.plot(responseTime)
#  plt.show()

# !! plt.subplot(3,1,1)
# !! plt.plot(responseTime)

# !! plt.subplot(3,1,2)
# !! plt.plot(processingTime)

# !! plt.subplot(3,1,3)
# !! plt.plot(responseTime/processingTime)
# !! plt.show()


# Wait for End process
#time.sleep(13)
while 0:
   pass
