import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np
from math import pi
plt.close('all')

# Generate sin wave
Fs = 1000
t = np.arange(0,1,1/Fs)
f = 20;

x = np.sin(2+pi*f*t)

plt.subplot(2,1,1)
plt.plot(t,x); plt.title('Sinusoidal Signal');
plt.xlabel('Time (in sec)'); plt.ylabel('Amplitude')

# Compute FFT
#X = fft(x)
#plt.subplot(2,1,2)
#plt.plot(abs(X))



