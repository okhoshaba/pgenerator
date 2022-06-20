# Examples 01
# From https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_quick_guide.htm

import _thread
import time
import os


def run_amplitude( threadName, delay, amplitude):
   count = 0
   while count < amplitude:
#   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s, %s: %s" % ( threadName, count, time.ctime(time.time()) ))

try:
   _thread.start_new_thread(run_amplitude, ("Amplitude = 1", 0.2, 10, ) )
#   os.system("echo Hello from the other side!")
   os.system("ls -l")
#   print("End generator 1")
   time.sleep(0.2)
   _thread.start_new_thread(run_amplitude, ("Amplitude == 2", 0.4, 5, ) )

#   print("End generator 2")
except:
   print ("Error run generator")

# print("End generator")


print("End generatorAll")

# Wait for End process
time.sleep(3)
while 0:
   pass
