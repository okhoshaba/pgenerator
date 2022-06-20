# Examples 01
# From https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm

import _thread
import time
import os

    # Internal cycles = intCount
def runAmplitude(threadName, amplitude):
   intCount = 0
   while intCount < amplitude:
#   while count < 5:
#   Not nesessary...
#      time.sleep(delay)
      intCount += 1
      print ("%s, %s: %s" % (threadName, intCount, time.ctime(time.time()) ))

try:
    # External cycles = extCount
   for extCount in range(6):
       _thread.start_new_thread(runAmplitude, (extCount, 10, ) )
       os.system("curl 192.168.222.19:9000 > /dev/null 2>&1")
       time.sleep(0.1)

except:
   print("Error run generator")

# Wait for End process
time.sleep(13)
while 0:
   pass
