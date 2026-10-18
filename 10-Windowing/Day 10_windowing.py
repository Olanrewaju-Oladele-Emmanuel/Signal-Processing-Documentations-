import numpy as np
import matplotlib.pyplot as plt

# Signal that causes leakage - 5.5Hz doesn't fit perfectly
fs = 100  # sampling
t = np.arange(0, 1, 1/fs)
f = 5.5 # non-integer freq = will leak
signal = np.sin(2 * np.pi * f * t)

# FFT without window
fft_no_window = np.fft.fft(signal)
freq = np.fft.fftfreq(len(t), 1/fs)

# Apply Hamming window
window = np.hamming(len(t))
signal_windowed = signal * window
fft_windowed = np.fft.fft(signal_windowed)

# Plot
plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.plot(t, signal, label='Original')
plt.plot(t, signal_windowed, label='Hamming Windowed')
plt.title('Day 10 - Effect of Windowing (5.5Hz signal)')
plt.legend()
plt.grid()

plt.subplot(3,1,2)
plt.stem(freq[:50], np.abs(fft_no_window)[:50])
plt.title('FFT without window - Leakage (messy)')
plt.grid()

plt.subplot(3,1,3)
plt.stem(freq[:50], np.abs(fft_windowed)[:50])
plt.title('FFT with Hamming Window - Leakage Reduced (cleaner)')
plt.grid()

plt.tight_layout()
plt.savefig('day10_windowing.png', dpi=150)
plt.show()
