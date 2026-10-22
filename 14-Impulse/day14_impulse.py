import numpy as np
import matplotlib.pyplot as plt

# day 14 - impulse response
# LTI system = h is the system

fs = 1000
t = np.linspace(0, 1, fs)

# my input, same 5hz i always use
f = 5
x = np.sin(2*np.pi*f*t)

# h - impulse response
# rc kind, exponential decay
tau = 0.05
h = np.exp(-t/tau)
h = h / sum(h)  # make small so y not too big

# output y = x * h
y = np.convolve(x, h, mode='same')

# 1st, 2nd and 3rd plots 
plt.figure(figsize=(9,6))

plt.subplot(3,1,1)
plt.plot(t, x)
plt.title('input x - 5hz sine')
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t, h)
plt.title('h - impulse response (RC exp) - this is the system')
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t, y)
plt.title('output y = x * h - smoothed')
plt.grid(True)

plt.tight_layout()
plt.savefig('day14_impulse.png', dpi=150)
plt.show()
