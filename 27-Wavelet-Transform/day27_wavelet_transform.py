mport numpy as np
import matplotlib.pyplot as plt

sampling_rate = 256
time_values = np.linspace(0, 1, sampling_rate)

signal = np.zeros_like(time_values)

for index in range(len(time_values)):
    if time_values[index] < 0.5:
        signal[index] = np.sin(2 * np.pi * 5 * time_values[index])
    else:
        signal[index] = np.sin(2 * np.pi * 20 * time_values[index])

# Add a spike at 0.75 seconds
signal[192] = signal[192] + 2.0
print(len(signal))

# Moving average for the low part
smooth_signal = np.zeros_like(signal)
for index in range(1, len(signal) - 1):
    smooth_signal[index] = (signal[index - 1] + signal[index] + signal[index + 1]) / 3
smooth_signal[0] = signal[0]
smooth_signal[-1] = signal[-1]

detail_signal = signal - smooth_signal
print("avg done")

scales = [4, 8, 16, 32]
wavelet_result = np.zeros((len(scales), len(signal)))

for scale_index, scale_value in enumerate(scales):
    wavelet_length = scale_value * 4
    wavelet_time = np.linspace(-4, 4, wavelet_length)
    wavelet = np.cos(5 * wavelet_time) * np.exp(-wavelet_time ** 2 / 2)

    for shift_position in range(len(signal)):
        total = 0
        for wavelet_index in range(len(wavelet)):
            signal_index = shift_position + wavelet_index - wavelet_length // 2
            if 0 <= signal_index < len(signal):
                total = total + signal[signal_index] * wavelet[wavelet_index]
        wavelet_result[scale_index, shift_position] = total / np.sqrt(scale_value)

plt.figure(figsize=(10, 9))

plt.subplot(4, 1, 1)
plt.plot(time_values, signal)
plt.title("Day 27 signal - 5Hz then 20Hz + spike")
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(time_values, smooth_signal, color="green")
plt.title("Low frequency part -- moving average")
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(time_values, detail_signal, color="red")
plt.title("High frequency part -- spike shows here")
plt.grid(True)

plt.subplot(4, 1, 4)
plt.imshow(np.abs(wavelet_result), aspect="auto", extent=[0, 1, 0, 4], cmap="jet")
plt.yticks([0, 1, 2, 3], ["32", "16", "8", "4"])
plt.xlabel("time")
plt.title("CWT scalogram")
plt.colorbar()

plt.tight_layout()
plt.show()
