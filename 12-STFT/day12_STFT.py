import numpy as np
import matplotlib.pyplot as plt

fs = 100
t = np.arange(0, 2, 1/fs)
signal = np.concatenate([np.sin(2*np.pi*5*t[:fs]), np.sin(2*np.pi*20*t[fs:])])

# STFT: cut into windows (Day 10 Windowing)
window_size = 32
hop = 8
window = np.hamming(window_size)

stft_matrix = []
for start in range(0, len(signal)-window_size, hop):
    seg = signal[start:start+window_size] * window
    fft_seg = np.abs(np.fft.rfft(seg))
    stft_matrix.append(fft_seg)

stft_matrix = np.array(stft_matrix).T
freqs = np.fft.rfftfreq(window_size, 1/fs)

plt.figure(figsize=(8,6))
plt.subplot(2,1,1)
plt.plot(t, signal)
plt.title('Day 12 - Signal: 5Hz then 20Hz')
plt.grid(True)

plt.subplot(2,1,2)
plt.imshow(20*np.log10(stft_matrix+1e-6), aspect='auto', origin='lower',
           extent=[0, 2, 0, fs/2], cmap='viridis')
plt.colorbar(label='Magnitude [dB]')
plt.title('STFT Spectrogram')
plt.xlabel('Time [s]'); plt.ylabel('Frequency [Hz]')
plt.tight_layout()
plt.savefig('day12_stft.png', dpi=200)
plt.show()
