# Day 30  #Grand Finale Final Capstone
# Noisy Signal -> Filter -> Modulate -> Recover

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, hilbert

fs = 1000
t = np.arange(0, 1.0, 1/fs)

# Original Signal
msg = np.sin(2 * np.pi * 5 * t)

# Add Noise
noisy = msg + 0.6 * np.sin(2 * np.pi * 50 * t) + 0.2 * np.random.randn(len(t))

# Filter With FIR
fir = firwin(51, 20, fs=fs, window='hamming')
filtered = lfilter(fir, 1.0, noisy)
delay = 25
filtered = np.roll(filtered, -delay)
filtered[-delay:] = filtered[-delay-1]

# Amplitude Modulation
fc = 100
carrier = np.cos(2 * np.pi * fc * t)
modulated = (1 + 0.8 * filtered) * carrier

# Demodulation And Recovery
envelope = np.abs(hilbert(modulated))
recovered = envelope - np.mean(envelope)
recovered = lfilter(fir, 1.0, recovered)
recovered = np.roll(recovered, -delay)
recovered[-delay:] = recovered[-delay-1]
recovered = recovered / np.max(np.abs(recovered)) * 0.9

print("Done")

# Plot
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(t, msg, color='blue')
plt.title('Day 30 Capstone: Noisy -> Filter -> Modulate -> Recover')
plt.ylabel('Original')
plt.grid(True)
plt.xlim(0, 0.6)

plt.subplot(4, 1, 2)
plt.plot(t, noisy, color='red', alpha=0.7)
plt.ylabel('Noisy')
plt.grid(True)
plt.xlim(0, 0.6)

plt.subplot(4, 1, 3)
plt.plot(t, filtered, color='green')
plt.ylabel('Filtered')
plt.grid(True)
plt.xlim(0, 0.6)

plt.subplot(4, 1, 4)
plt.plot(t, msg, color='blue', linestyle='--', label='Original')
plt.plot(t, recovered, color='purple', label='Recovered')
plt.ylabel('Recovered')
plt.xlabel('Time [s]')
plt.legend()
plt.grid(True)
plt.xlim(0, 0.6)

plt.tight_layout()
plt.savefig('Day30_Final_Capstone.png', dpi=150)
plt.show()
