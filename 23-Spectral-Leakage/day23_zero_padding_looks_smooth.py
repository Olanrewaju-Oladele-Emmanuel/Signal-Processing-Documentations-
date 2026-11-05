import numpy as np
import matplotlib.pyplot as plt

fs = 100
N = 100
t = np.arange(N)/fs
x2 = np.sin(2*np.pi*10.5*t)
w = np.hanning(N)
x2_win = x2 * w

# Zero padding, It just makes it look smooth
X_nopad = abs(np.fft.rfft(x2_win))
X_pad = abs(np.fft.rfft(x2_win, n=1024))
f = np.fft.rfftfreq(N, 1/fs)
f_pad = np.fft.rfftfreq(1024, 1/fs)

plt.figure(figsize=(10,4))
plt.suptitle("Zero Padding - Same Info, Just Smoother")
plt.subplot(1,2,1)
plt.stem(f, X_nopad)
plt.title("No Padding")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.subplot(1,2,2)
plt.plot(f_pad, X_pad)
plt.title("Padded to 1024")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.tight_layout()
plt.savefig("zero_padding_smooth_look.png")
plt.show()
