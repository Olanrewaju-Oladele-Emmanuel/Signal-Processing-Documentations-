import numpy as np
import matplotlib.pyplot as plt

# Day 18 - IIR filter, finally

fs = 100
t = np.linspace(0, 2, 2*fs)

# my signal, 5hz + 50hz noise
clean = np.sin(2*np.pi*5*t)
noise = np.sin(2*np.pi*50*t)
noisy = clean + 0.8*noise

print("signal created")

# IIR low pass
# y[n] = alpha*x[n] + (1-alpha)*y[n-1]
# this feedback part is diff from FIR
fc = 15
alpha = 1 - np.exp(-2*np.pi*fc/fs)
print(f"alpha = {alpha}")

y = np.zeros(len(t))
y[0] = noisy[0]

for n in range(1, len(t)):
    y[n] = alpha*noisy[n] + (1-alpha)*y[n-1]

# second order try, coefficients from online calculator for 15hz
# b0,b1,b2 and a1,a2
b0 = 0.067
b1 = 0.134
b2 = 0.067
a1 = -1.143
a2 = 0.412

y2 = np.zeros(len(t))
for n in range(2, len(t)):
    y2[n] = b0*noisy[n] + b1*noisy[n-1] + b2*noisy[n-2] - a1*y2[n-1] - a2*y2[n-2]

print("filtering done")

# plot
plt.figure(figsize=(10,6))

plt.subplot(3,1,1)
plt.plot(t, noisy, 'r', label='noisy')
plt.plot(t, clean, 'k--', label='clean 5hz')
plt.legend()
plt.grid(True)
plt.xlim(0,1)
plt.title("Input 5hz + 50hz")

plt.subplot(3,1,2)
plt.plot(t, y, label='1st order')
plt.plot(t, y2, label='2nd order iir')
plt.legend()
plt.grid(True)
plt.xlim(0,1)
plt.title("After IIR low pass fc=15hz")

plt.subplot(3,1,3)
# check freq
fft_noisy = np.abs(np.fft.fft(noisy))
fft_y2 = np.abs(np.fft.fft(y2))
freqs = np.fft.fftfreq(len(t), 1/fs)

plt.plot(freqs[:50], fft_noisy[:50], 'r', label='before')
plt.plot(freqs[:50], fft_y2[:50], 'g', label='after')
plt.legend()
plt.grid(True)
plt.xlabel("freq hz")

plt.tight_layout()
plt.savefig("day18_iir.png", dpi=150)
plt.show()

print("day 18 done")
