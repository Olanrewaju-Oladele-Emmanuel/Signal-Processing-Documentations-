import numpy as np
import matplotlib.pyplot as plt

# Parameters - same as Day 07
f = 5 # Hz - main frequency
fs = 500 # Sampling rate
T = 1 # Duration 1 second
t = np.linspace(0, T, int(fs*T), endpoint=False)

# Signal: Our Day 07 superposition (5Hz + 3*5Hz) + a 50Hz noise
signal = np.sin(2*np.pi*f*t) + 0.5*np.sin(2*np.pi*3*f*t) + 0.3*np.sin(2*np.pi*50*t)

# FOURIER TRANSFORM - The Magic
N = len(signal)
fft_result = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(N, 1/fs)
magnitude = np.abs(fft_result) / N

# Plot
plt.figure(figsize=(10, 6))

# Time Domain (What you see on oscilloscope)
plt.subplot(2,1,1)
plt.plot(t[:200], signal[:200])
plt.title('Day 08 - Time Domain: What the signal looks like')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Frequency Domain (What FFT reveals)
plt.subplot(2,1,2)
plt.stem(fft_freq[:N//2], magnitude[:N//2]*2, basefmt=" ")
plt.title('Frequency Domain: What frequencies are inside')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.xlim(0, 60)
plt.grid(True)

plt.tight_layout()
plt.savefig('day08_fourier_transform.png', dpi=150)
plt.show()

# Print peaks
print("Peaks found at:")
for freq, mag in zip(fft_freq[:N//2], magnitude[:N//2]*2):
    if mag > 0.1:
        print(f"{freq:.1f} Hz -> {mag:.2f}")
