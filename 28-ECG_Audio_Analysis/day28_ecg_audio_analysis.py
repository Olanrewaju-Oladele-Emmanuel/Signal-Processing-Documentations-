# Day 28
# ecg + audio
# I wanted to see if I can clean a noisy ecg and find heart rate
import numpy as np
import matplotlib.pyplot as plt

fs = 360
t = np.arange(0, 10, 1/fs)
np.random.seed(7) # Change this if you want different noise

# Make one heartbeat shape
def one_beat(tb):
    p = 0.15 * np.exp(-((tb - 0.15)**2) / (2 * 0.02**2))
    qrs = 1.0 * np.exp(-((tb - 0.30)**2) / (2 * 0.01**2))
    t_wave = 0.25 * np.exp(-((tb - 0.50)**2) / (2 * 0.03**2))
    return p + qrs + t_wave

ecg = np.zeros(len(t))
# 72 bpm
for start in np.arange(0, 10, 60/72):
    m = (t >= start) & (t < start + 0.8)
    ecg[m] = ecg[m] + one_beat(t[m] - start)

# Add noise like in real life
wander = 0.2 * np.sin(2*np.pi*0.3*t)
noise = 0.05 * np.random.randn(len(t))
power = 0.05 * np.sin(2*np.pi*50*t)
ecg_noisy = ecg + wander + noise + power

# My filter, ust moving average to remove wander
def smooth(x, w):
    return np.convolve(x, np.ones(w)/w, mode='same')

base = smooth(ecg_noisy, 101)
ecg_clean2 = smooth(ecg_noisy - base, 5)

# Find peaks
thresh = 0.6 * max(ecg_clean2)
peaks = []
last = -200
for i in range(1, len(ecg_clean2)-1):
    if ecg_clean2[i] > ecg_clean2[i-1] and ecg_clean2[i] > ecg_clean2[i+1]:
        if ecg_clean2[i] > thresh and i - last > 180:
            peaks.append(i)
            last = i

peaks = np.array(peaks)
rr = np.diff(t[peaks])
hr = 60 / np.mean(rr)
print("beats found:", len(peaks))
print("heart rate:", round(hr, 1), "bpm")
print("avg RR:", round(np.mean(rr)*1000, 1), "ms")
print("hrv:", round(np.std(rr)*1000, 1), "ms")

# Audio part: simple chirp
fs2 = 8000
ta = np.arange(0, 2, 1/fs2)
audio = np.sin(2*np.pi*(200 + 300*ta)*ta) + 0.3*np.random.randn(len(ta))

# STFT by hand, from day 12
win = np.hanning(256)
spec = []
for n in range(0, len(audio)-256, 128):
    frame = audio[n:n+256] * win
    spec.append(np.abs(np.fft.rfft(frame)))
spec = np.array(spec).T

# Plots
plt.figure(figsize=(10, 8))

plt.subplot(3,1,1)
plt.plot(t, ecg_noisy, color='gray', linewidth=0.7, label='noisy')
plt.plot(t, ecg_clean2, color='blue', label='filtered')
plt.plot(t[peaks], ecg_clean2[peaks], 'ro', label='peaks')
plt.title(f"ECG - HR {hr:.1f} bpm")
plt.legend()
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(ta[:2000], audio[:2000], color='green')
plt.title("Audio chirp 200 to 800 Hz")
plt.grid(True)

plt.subplot(3,1,3)
plt.imshow(20*np.log10(spec + 1e-6), aspect='auto', origin='lower', cmap='viridis')
plt.title("Spectrogram - frequency going up")
plt.colorbar()

plt.tight_layout()
plt.savefig("day28_result.png")
plt.show()
