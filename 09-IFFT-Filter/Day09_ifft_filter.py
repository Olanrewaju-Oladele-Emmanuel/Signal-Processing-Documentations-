import numpy as np
import matplotlib.pyplot as plt

# 1. Create a noisy signal (same as Day 8)
fs = 500  # sampling rate
t = np.arange(0, 1, 1/fs)  # 1 second
clean = np.sin(2*np.pi*5*t)  # 5Hz real signal
noise = 0.5*np.sin(2*np.pi*50*t)  # 50Hz noise (like powerline)
noisy = clean + noise

# 2. FFT - Go to frequency domain
fft_vals = np.fft.fft(noisy)
freqs = np.fft.fftfreq(len(t), 1/fs)

# 3. FILTER in frequency domain - Kill the 50Hz noise
# Create copy and set 50Hz bins to zero
fft_filtered = fft_vals.copy()
# Find indices where freq is around 50Hz
fft_filtered[(np.abs(freqs) > 45) & (np.abs(freqs) < 55)] = 0

# 4. IFFT - Come back to time domain
cleaned_signal = np.fft.ifft(fft_filtered)
cleaned_signal = np.real(cleaned_signal)  # take real part

# 5. Plot all 3
plt.figure(figsize=(10,6))
plt.subplot(3,1,1)
plt.plot(t, noisy)
plt.title("Day 9 - Original Noisy Signal (5Hz + 50Hz)")
plt.subplot(3,1,2)
plt.plot(freqs[:250], np.abs(fft_vals[:250]))
plt.title("FFT - See 2 peaks at 5Hz and 50Hz")
plt.subplot(3,1,3)
plt.plot(t, cleaned_signal)
plt.title("After IFFT - Clean 5Hz Recovered")
plt.tight_layout()
plt.savefig("day09_ifft_filter.png")
plt.show()

print("Day 9 Done. Filtering by FFT + IFFT successful.")
