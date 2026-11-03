Day 22: Noisy Signal

I wanted to see what noise does to a clean signal.

I generated a 50Hz sine wave as the clean signal with fs = 1000.
Then I added random noise to it. That is the kind of noisy signal we see in real life.

I calculated the signal power and noise power and then the SNR.
My SNR is -1.0 dB. It is very low. The noise has covered the signal.

The first plot is the clean signal. The second plot is the noisy signal. You can see the difference.

I will try to filter it tomorrow.

code - day22_noise_snr.py
plot - day22_noise_snr.png
