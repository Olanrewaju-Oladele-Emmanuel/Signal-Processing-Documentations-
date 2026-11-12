# Day 29 
# Filter Comparison Project
# I Wanted To Compare Everything From Day 17 And Day 18, I Used The Same Signal Again So The Comparison Is Fair

import numpy as np
import matplotlib.pyplot as plt

# I Made My Signal Again, 5Hz Clean Plus 50Hz Noise
fs = 500
t = np.arange(0, 1, 1/fs)
clean = np.sin(2*np.pi*5*t)
x = clean + 0.8*np.sin(2*np.pi*50*t)

# I Did FIR First, Moving Average With 20 Taps Like Day 17
fir = np.convolve(x, np.ones(20)/20, mode='same')

# I Did IIR 1st Order Next, Same Formula From Day 18
alpha = 1 - np.exp(-2*np.pi*15/fs)
iir1 = np.zeros_like(x)
for n in range(1, len(x)):
    iir1[n] = alpha*x[n] + (1-alpha)*iir1[n-1]
iir1[0] = x[0]

# I Did IIR 2nd Order Last, I Copied These Numbers From Day 18, Although I Did Not Check If They Were For fs = 500
b0, b1, b2 = 0.067, 0.134, 0.067
a1, a2 = -1.143, 0.412
iir2 = np.zeros_like(x)
for n in range(2, len(x)):
    iir2[n] = b0*x[n] + b1*x[n-1] + b2*x[n-2] - a1*iir2[n-1] - a2*iir2[n-2]
iir2[0] = x[0]
iir2[1] = x[1]

# I Checked Error By Comparing Each Output To The Clean Signal
def my_error(y):
    return np.sqrt(np.mean((y - clean)**2))

print("No filter:", round(float(my_error(x)), 4))
print("FIR:", round(float(my_error(fir)), 4))
print("IIR1:", round(float(my_error(iir1)), 4))
print("IIR2:", round(float(my_error(iir2)), 4))

# I Plotted All 4 So I Can See Which One Is Cleanest
plt.figure(figsize=(10, 8))

plt.subplot(4, 1, 1)
plt.plot(t, x, color='red')
plt.plot(t, clean, color='black', linestyle='--', linewidth=1)
plt.title('Original')
plt.ylabel('amp')

plt.subplot(4, 1, 2)
plt.plot(t, fir, color='blue')
plt.plot(t, clean, color='black', linestyle='--', linewidth=1)
plt.title('FIR 20 taps')
plt.ylabel('amp')

plt.subplot(4, 1, 3)
plt.plot(t, iir1, color='green')
plt.plot(t, clean, color='black', linestyle='--', linewidth=1)
plt.title('IIR 1st order')
plt.ylabel('amp')

plt.subplot(4, 1, 4)
plt.plot(t, iir2, color='purple')
plt.plot(t, clean, color='black', linestyle='--', linewidth=1)
plt.title('IIR 2nd order')
plt.xlabel('time (s)')
plt.ylabel('amp')

plt.tight_layout()
plt.savefig('day29_filter_comparison.png', dpi=150)
plt.show()
