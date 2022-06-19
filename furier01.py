# https://www.youtube.com/watch?v=su9YSmwZmPg&ab_channel=FluidicColours
# NumPy Tutorials : 011 : Fast Fourier Transforms - FFT and IFFT

import imp
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft

n = 1000
Lx = 100
omg = 2.0 * np.pi/Lx

x = np.linspace(0, Lx, n)


#print(x)


