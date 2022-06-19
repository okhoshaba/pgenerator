import numpy as np
from scipy import fftpack

time_step = 0.05
time_vec = np.arange(0, 10, time_step)

period = 5

sig = (np.sin(2*np.pi*time_vec/period) + 0.25 * np.random.randn(time_vec.size))

sig_fft = fftpack.fft(sig)

Amplitude = np.abs(sig_fft)
Power = Amplitude**2
Angle = np.angle(sig_fft)

sample_freq = fftpack.fftfreq(sig.size, d=time_step)

Amp_Freq = np.array([Amplitude, sample_freq])

Amp_position = Amp_Freq[0,:].argmax()

peak_freq = Amp_Freq[1, Amp_position]

print(Amp_position)
print(peak_freq)

high_freq_fft = sig_fft.copy()
high_freq_fft[np.abs(sample_freq) > peak_freq] = 0
print(high_freq_fft)

#print(Amplitude)
#print(sample_freq)

#print(period)
#print(np.round(sig,2))
