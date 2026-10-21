import numpy as np
import matplotlib.pyplot as plt

# day 13
# checking if signal looks like itself

fs = 100  # sample rate
t = np.linspace(0, 2, 2*fs, endpoint=False)

# 5hz wave
x = np.sin(2*np.pi*5*t)

# make same wave but shift it a bit
delay_samples = 10
y = np.roll(x, delay_samples)  # this shifts it

# now do correlation
# x vs x should peak at 0
autocorr = np.correlate(x, x, mode='full')
lags_auto = np.arange(-len(x)+1, len(x))

# x vs y should show the delay
crosscorr = np.correlate(x, y, mode='full')
lags_cross = np.arange(-len(x)+1, len(x))

# plot everything
plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(t, x, label='x = 5hz sine')
plt.plot(t, y, '--', label=f'y = delayed by {delay_samples} samples')
plt.legend()
plt.title('Day 13 - Original vs Delayed Signal')
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(lags_auto, autocorr)
plt.title('Autocorrelation of x - Peak at 0 lag = signal matches itself')
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(lags_cross, crosscorr)
plt.title(f'Cross-correlation x vs y - Peak shows delay at {delay_samples} samples')
plt.grid(True)

plt.tight_layout()
plt.savefig('day13_correlation.png', dpi=150)
plt.show()

# find the delay from the peak
peak_index = np.argmax(crosscorr)
estimated_delay = lags_cross[peak_index]
print(f"True delay: {delay_samples} samples")
print(f"Estimated delay: {estimated_delay} samples")
