# Day 25: Hilbert Transform and Envelope
# I am trying to get the envelope of an AM signal

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

# I set my sampling frequency to 1000
fs = 1000
t = np.arange(0, 1, 1/fs)

# My message is 5 Hz and my carrier is 50 Hz
message = np.cos(2 * np.pi * 5 * t)
carrier = np.cos(2 * np.pi * 50 * t)

# This is my AM signal
am = (1 + 0.8 * message) * carrier

# Here I used Hilbert to get the analytic signal
analytic = hilbert(am)
envelope = abs(analytic) # this is the envelope

print("I got the envelope")
print("Max of envelope is", max(envelope))
print("Min of envelope is", min(envelope))

# First plot: AM signal and envelope
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, am, label="AM signal")
plt.plot(t, envelope, label="Envelope", color="red")
plt.plot(t, -envelope, color="red")
plt.title("Day 25: AM Signal and its Envelope")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Second plot: I wanted to see if I can get my message back
plt.subplot(2, 1, 2)
plt.plot(t, message, label="Original message")
plt.plot(t, envelope - 1, label="Message from envelope", linestyle="--")
plt.title("Original message vs Recovered message")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
