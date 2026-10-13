# Day 07 - Fourier Series
# Name: Olanrewaju Oladele Emmanuel
# Trying to build square wave from sine waves

import numpy as np
import matplotlib.pyplot as plt

# time base
t = np.linspace(0, 1, 1000)
f = 1 # fundamental 1Hz
T = 1/f # period = 1s

# Fourier series for square wave
# 4/pi * sum(sin(2*pi*(2k-1)*f*t)/(2k-1))
# using 1,3,5,7,9 harmonics

y = np.zeros_like(t)
y += np.sin(2*np.pi*1*f*t)/1
y += np.sin(2*np.pi*3*f*t)/3
y += np.sin(2*np.pi*5*f*t)/5
y += np.sin(2*np.pi*7*f*t)/7
y += np.sin(2*np.pi*9*f*t)/9

y = (4/np.pi) * y

plt.figure()
plt.plot(t, y, label='Fourier 5 terms (1,3,5,7,9)')
plt.axhline(1, color='red', linestyle='--', alpha=0.5)
plt.axhline(-1, color='red', linestyle='--', alpha=0.5)
plt.title('Day 07: Fourier Series Square Wave\nf=1Hz T=1s Harmonics 1,3,5,7,9')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.savefig('day07_fourier.png')
plt.show()

print(f"f={f}Hz, T={T}s, 5 harmonics used")
