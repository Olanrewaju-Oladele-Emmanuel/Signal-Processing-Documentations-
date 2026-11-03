import numpy as np
import matplotlib.pyplot as plt

# My  signal
fs = 1000  # Sampling
t = np.linspace(0, 1, fs)

# Clean 50Hz sine wave/signal
clean = np.sin(2*np.pi*50*t)

# Added noise - this is what happens in real life scenario 
noise = np.random.randn(len(t)) * 0.8
noisy = clean + noise

# Find SNR
ps = np.mean(clean**2)
pn = np.mean(noise**2)
snr = 10*np.log10(ps/pn)

print("Signal power:", round(ps,3))
print("Noise power:", round(pn,3))
print("My SNR is", round(snr,2), "dB")

# Plot am
plt.figure()

# First plot, clean signal 
plt.subplot(2,1,1)
plt.plot(t[0:200], clean[0:200])
plt.title("Clean Signal - 50Hz")
plt.ylabel("Amplitude")

# Second plot noisy
plt.subplot(2,1,2)
plt.plot(t[0:200], noisy[0:200], color='red')
plt.title(f"Noisy Signal - SNR {round(snr,1)} dB")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
