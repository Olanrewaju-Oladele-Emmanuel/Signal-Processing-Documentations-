import numpy as np
import matplotlib.pyplot as plt

fs = 100
N = 100
t = np.arange(N)/fs

# The 10Hz one fits
x1 = np.sin(2*np.pi*10*t)
# The 10.5 one doesnt fit, this is the one that causes trouble
x2 = np.sin(2*np.pi*10.5*t)

X1 = abs(np.fft.rfft(x1))
X2 = abs(np.fft.rfft(x2))
f = np.fft.rfftfreq(N, 1/fs)

plt.figure(figsize=(10,4))
plt.suptitle("Spectral Leakage - 10Hz vs 10.5Hz")
plt.subplot(1,2,1)
plt.stem(f, X1)
plt.title("10 Hz - Fits")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.subplot(1,2,2)
plt.stem(f, X2)
plt.title("10.5 Hz - Leaks")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("leakage_10_vs_10p5.png")
plt.show()
