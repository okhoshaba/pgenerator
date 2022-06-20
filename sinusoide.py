# https://ru.stackoverflow.com/questions/1334425/%D0%9F%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D1%81%D0%B8%D0%BD%D1%83%D1%81%D0%BE%D0%B8%D0%B4%D1%83
# Построить-синусоиду

import numpy as np
import matplotlib.pyplot as plt

basis = 20
amplitudes = 10
Fs = 500
f = 5
sample = 200
t = np.arange(sample)
quer = basis + np.sin(2 * np.pi * f * t / Fs) * amplitudes
#y = np.sin(2 * np.pi * f * x / Fs) * 10 + 20

print(quer)
print(quer[2])
plt.plot(quer)
plt.show()

