import numpy as np
import matplotlib.pyplot as plt

# I made a simple signal, 5 Hz sine wave, I used high rate for the original so it looks smooth
t_original = np.linspace(0, 1, 1000)
original = np.sin(2 * np.pi * 5 * t_original)

# Now I sampled it, I used 50 Hz sampling,  50 is more than 2 times 5, so Nyquist is satisfied
fs = 50
t_sampled = np.arange(0, 1, 1/fs)
sampled = np.sin(2 * np.pi * 5 * t_sampled)

# This is the reconstruction part, I used sinc interpolation, each sample makes a sinc and we add them
reconstructed = np.zeros_like(t_original)
for i in range(len(t_sampled)):
    reconstructed = reconstructed + sampled[i] * np.sinc((t_original - t_sampled[i]) * fs)

print("I took", len(t_sampled), "samples")
print("Original and reconstructed look almost the same")
print("Max error is", max(abs(original - reconstructed)))

# Plot
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t_original, original, label="Original signal")
plt.stem(t_sampled, sampled, label="Samples I took", linefmt="r-", markerfmt="ro", basefmt=" ")
plt.title("Day 26: Original signal and my samples")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t_original, original, label="Original")
plt.plot(t_original, reconstructed, label="Reconstructed", linestyle="--")
plt.title("Original vs Reconstructed - they match")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

