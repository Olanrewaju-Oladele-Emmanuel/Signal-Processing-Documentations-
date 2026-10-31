import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

fs = 1000
t = np.arange(0, 1, 1/fs)

# This is my test signal, I added 10Hz, 80Hz and 200Hz together
s = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*80*t) + np.sin(2*np.pi*200*t)

# High pass filter, I set it at 50Hz so it will remove the low 10Hz
b,a = butter(4, 50, 'highpass', fs=fs)
hp = lfilter(b,a,s)

# Band pass from 60 to 120Hz, so only 80Hz will remain
b2,a2 = butter(4, [60,120], 'bandpass', fs=fs)
bp = lfilter(b2,a2,s)

# Plotting all three together on one screen
plt.figure(figsize=(8,6))

plt.subplot(3,1,1) # first plot
plt.plot(t[:250], s[:250])
plt.title("1. original signal")
plt.ylabel("amp")


 # Second one is highpass
plt.subplot(3,1,2) 
plt.plot(t[:250], hp[:250], 'r')
plt.title("2. highpass filtered")
plt.ylabel("amp")

plt.subplot(3,1,3) # Third one is bandpass
plt.plot(t[:250], bp[:250], 'g')
plt.title("3. bandpass filtered")
plt.xlabel("time")
plt.ylabel("amp")

# So  they don't overlap 
plt.tight_layout()
plt.show()
