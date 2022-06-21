# https://stackoverflow.com/questions/25735153/plotting-a-fast-fourier-transform-in-python

import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# 2. Integer number of periods
N = 1000
tmax = 1
T = tmax / N # Sample spacing
x2 = np.linspace(0.0, N*T, N)
y2 = 38 * np.sin(50.0 * 2.0*np.pi*x2)
yf2 = scipy.fftpack.fft(y2)
xf2 = np.linspace(0.0, 1.0/(2.0*T), N//2)

ymax = max(2.0/N * np.abs(yf2[:N//2]))
print(ymax)
print(x2)
print(T)

fig, ax = plt.subplots()
# Plotting only the left part of the spectrum to not show aliasing
#ax.plot(xf1, 2.0/N * np.abs(yf1[:N//2]), label='fftpack tutorial')
ax.plot(xf2, 2.0/N * np.abs(yf2[:N//2]), label='Integer number of periods')
#ax.plot(xf3, 2.0/N * np.abs(yf3[:N//2]), label='Correct positioning of dates')
plt.legend()
plt.grid()
plt.show()

