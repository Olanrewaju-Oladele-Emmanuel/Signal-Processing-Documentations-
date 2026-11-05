import numpy as np
import matplotlib.pyplot as plt

fs = 100
n = 100
tt = np.arange(n)/fs
xx = np.sin(2*np.pi*10*tt) + np.sin(2*np.pi*12*tt)
XX = abs(np.fft.rfft(xx * np.hanning(n)))
ff = np.fft.rfftfreq(n, 1/fs)

# Last test, 10 and 12 together, With N=100 I can't separate them, they just merge
plt.figure()
plt.title("10Hz + 12Hz, N=100 - Merged Into One Peak")
plt.plot(ff, XX)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0,30)
plt.grid(True)
plt.savefig("two_tones_10_and_12_N100.png")
plt.show()
