import numpy as np
import matplotlib.pyplot as plt

fs = 100
N = 100
t = np.arange(N)/fs
x2 = np.sin(2*np.pi*10.5*t)

# Hann stuff: Basically it makes the ends go to zero so FFT doesnt see a jump
w = np.hanning(N)
x2_win = x2 * w

X2 = abs(np.fft.rfft(x2))
X2_win = abs(np.fft.rfft(x2_win))
f = np.fft.rfftfreq(N, 1/fs)

plt.figure(figsize=(10,4))
plt.suptitle("Hann Window Reduces Leakage")
plt.subplot(1,2,1)
plt.stem(f, X2)
plt.title("No Window - Leaks Everywhere")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.subplot(1,2,2)
plt.stem(f, X2_win, linefmt='r-', markerfmt='ro')
plt.title("Hann Window - Clean Peak")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("hann_vs_no_window.png")
plt.show()
