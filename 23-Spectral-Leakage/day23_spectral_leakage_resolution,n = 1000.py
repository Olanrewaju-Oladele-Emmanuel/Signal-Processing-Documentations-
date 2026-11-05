import numpy as np
import matplotlib.pyplot as plt

fs = 100
n = 1000
tt = np.arange(n)/fs
xx = np.sin(2*np.pi*10*tt) + np.sin(2*np.pi*12*tt)
XX = abs(np.fft.rfft(xx * np.hanning(n)))
ff = np.fft.rfftfreq(n, 1/fs)

# Same test but with N=1000, now I can actually see two separate peaks
plt.figure()
plt.title("10Hz + 12Hz, N=1000 - Two Separate Peaks")
plt.plot(ff, XX)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0,30)
plt.grid(True)
plt.savefig("two_tones_10_and_12_N1000.png")
plt.show()
