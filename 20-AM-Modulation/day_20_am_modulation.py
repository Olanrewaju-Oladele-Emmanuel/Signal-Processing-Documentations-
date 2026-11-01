import numpy as np
import matplotlib.pyplot as plt

# setting my frequencies first
fm = 5   # this is my message, it's slow, like voice
fc = 50  # this is the carrier, it's fast
fs = 1000
t = np.arange(0, 1, 1/fs) # just 1 second, so it's not too long'

m = 0.8  # the modulation index, if it is more than 1 it will distort

# my message,  I used cosine, it's' simple
message = np.cos(2 * np.pi * fm * t)

# carrier , it's also cosine but faster
carrier = np.cos(2 * np.pi * fc * t)

#  This is the main AM formula
# AM formula is this: (1 + m*message) * carrier
am_signal = (1 + m * message) * carrier

# Here I plot  3 graphs
plt.figure(figsize=(10, 8))

plt.subplot(3,1,1)
plt.plot(t, message, 'b')
plt.title('My Message = 5Hz')
plt.ylabel('Amplitude')
plt.grid(True) # added grid so it's clear

plt.subplot(3,1,2)
plt.plot(t, carrier, 'g')
plt.title('Carrier =  50Hz, fast one')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t, am_signal, 'r') # this is the main AM signal
plt.plot(t, 1 + m*message, 'k--') # upper envelope
plt.plot(t, -(1 + m*message), 'k--') # lower
plt.title('AM Signal: observe how it  follows the message')
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout() # to prevent overlap
plt.show()

print(", the envelope is the message shape")
