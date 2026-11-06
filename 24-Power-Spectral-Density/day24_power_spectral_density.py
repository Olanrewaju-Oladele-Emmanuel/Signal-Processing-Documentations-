import numpy as np
import matplotlib.pyplot as plt

# I did not understand PSD before today, so I am just trying it out

fs = 1000 # I am using 1000 because it is easy to work with
t = np.arange(0, 2, 1/fs)

# My signal: 5Hz is loud, 20Hz is quiet, plus some noise, I hope this works
sig = 2*np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*20*t) + 0.5*np.random.randn(len(t))

# First one, the simple one, Do FFT, square it to get power, then divide by fs*N. Divide by N to average it, so longer signal does not look louder.  Divide by fs to get power per 1 Hz, not just total power
N = len(sig)
X = np.fft.rfft(sig * np.hanning(N)) # Hann window from Day 10, if I do not use it the spectrum will leak
freqs = np.fft.rfftfreq(N, 1/fs)
psd_simple = (abs(X)**2) / (fs * N)

# Second one, Welch, cut it into small pieces and then average them
#Someone on YouTube said averaging will reduce the noise, let me see if it is true
def my_welch(x, fs, chunk=256):
    step = chunk // 2 # Half overlap
    win = np.hanning(chunk)
    total = 0
    how_many = 0
    for start in range(0, len(x)-chunk+1, step):
        piece = x[start:start+chunk] * win
        Xp = np.fft.rfft(piece)
        total += (abs(Xp)**2) / (fs * np.sum(win**2))
        how_many += 1
    f = np.fft.rfftfreq(chunk, 1/fs)
    return f, total / how_many

freqs2, psd_welch = my_welch(sig, fs)

# Plot time, three plots on one page
plt.figure(figsize=(10, 7))

plt.subplot(3,1,1)
plt.plot(t[:500], sig[:500])
plt.title("My signal, it looks a bit messy")
plt.ylabel("Amplitude")
plt.grid(True)
plt.xlim(0, 0.5)

plt.subplot(3,1,2)
plt.plot(freqs, 10*np.log10(psd_simple + 1e-12))
plt.title("Simple PSD, there is noise everywhere")
plt.ylabel("Power (dB)")
plt.grid(True)
plt.xlim(0, 50)

plt.subplot(3,1,3)
plt.plot(freqs2, 10*np.log10(psd_welch + 1e-12), color='red', linewidth=2)
plt.title("Welch PSD, this one is much cleaner")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power (dB)")
plt.grid(True)
plt.xlim(0, 50)

plt.tight_layout()
plt.show()

# Let me check, 5Hz should be bigger than 20Hz
i5 = np.argmin(abs(freqs2 - 5))
i20 = np.argmin(abs(freqs2 - 20))
print("5Hz:", round(10*np.log10(psd_welch[i5]), 1), "dB")
print("20Hz:", round(10*np.log10(psd_welch[i20]), 1), "dB")
print("It worked, 5Hz is bigger")
