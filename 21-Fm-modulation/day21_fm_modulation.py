import numpy as np
import matplotlib.pyplot as plt

# 5hz message, 50hz carrier

fs = 1000
t = np.arange(0, 1, 1/fs)

# Message; 5hz, low frequency 
msg = np.cos(2*np.pi*5*t)  

# Carrier; 50hz, high frequency 
car = np.cos(2*np.pi*50*t) 

# Fm modulation and Formula
# cos(2pi * fc * t + kf/fm * sin(2pi * fm * t))
kf = 20
fm = 5
fc = 50

fm_sig = np.cos(2*np.pi*fc*t + (kf/fm)*np.sin(2*np.pi*fm*t))

# Plots
plt.figure(figsize=(9,7))

plt.subplot(4,1,1)
plt.plot(t, msg)
plt.title("message 5hz")
plt.grid(True)

plt.subplot(4,1,2)
plt.plot(t, car)
plt.title("carrier 50hz")
plt.grid(True)

plt.subplot(4,1,3)
plt.plot(t, fm_sig, color='r')
plt.title("fm modulated")
plt.grid(True)

plt.subplot(4,1,4)
# Frequency goes up and down with message 
inst_freq = fc + kf*msg
plt.plot(t, inst_freq, color='purple')
plt.title("instant frequency 30 to 70 hz")
plt.xlabel("time")
plt.grid(True)

plt.tight_layout()
plt.show()
