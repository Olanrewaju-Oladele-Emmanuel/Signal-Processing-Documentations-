import numpy as np
import matplotlib.pyplot as plt


fs = 200  # sampling rate
fc = 20   # cutoff frequency
N = 51
M = (N-1)//2
n = np.arange(N)

# full sinc formula without np.sinc
# h = sin(2*pi*fc*(n-M)/fs) / (pi*(n-M))
# at center n=M we avoid divide by zero
h_ideal = np.zeros(N)
for i in range(N):
    x = n[i] - M
    if x == 0:
        h_ideal[i] = 2*fc/fs
    else:
        h_ideal[i] = np.sin(2*np.pi*fc*x/fs) / (np.pi*x)

# hamming window
w = np.zeros(N)
for i in range(N):
    w[i] = 0.54 - 0.46 * np.cos(2*np.pi*i/(N-1))

h = h_ideal * w
h = h / np.sum(h)

print(h[:5])

# rest same
freqs = np.linspace(0, 100, 512)
H = []
for f in freqs:
    r = 0
    im = 0
    for k in range(N):
        r += h[k]*np.cos(2*np.pi*f*k/fs)
        im -= h[k]*np.sin(2*np.pi*f*k/fs)
    H.append((r*r + im*im)**0.5)

t = np.arange(0, 1, 1/fs)
x = np.sin(2*np.pi*5*t) + 0.8*np.sin(2*np.pi*50*t)

y = np.zeros(len(t))
for i in range(len(t)):
    s = 0
    for j in range(N):
        if i-j >= 0:
            s += x[i-j]*h[j]
    y[i] = s

plt.figure()
plt.subplot(2,1,1)
plt.plot(freqs, H)
plt.title('day 17 fir filter- full sinc')
plt.grid()
plt.subplot(2,1,2)
plt.plot(t, x, label='in')
plt.plot(t, y, label='out')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
