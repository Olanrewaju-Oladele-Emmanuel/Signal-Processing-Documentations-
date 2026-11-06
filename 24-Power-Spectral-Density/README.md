Day 24: Power Spectral Density

Today, I finished this after like 2 hours.

What I was trying to do:
I wanted to understand PSD. Before today I kept mixing it up with FFT. FFT tells me what frequencies are there. PSD tells me how much power is in each frequency.

What I did:
I made a signal with 5 Hz amplitude 2 which is loud, 20 Hz amplitude 0.5 which is quiet, plus some random noise. Then I did two things. First, simple PSD, just FFT, square it, divide. Second, Welch PSD, cut the signal into small pieces, do PSD for each piece, then average them.

What confused me:
I did not understand why we divide by fs times N. I thought it was just a formula from the book. I later understood it. We divide by N to average it, so a longer signal does not look louder. We divide by fs to get power per 1 Hz, not just total power. That part took me the longest.

What I saw in the plot:
The simple PSD had the right peaks at 5 Hz and 20 Hz, but it was very noisy. The Welch PSD was much cleaner. The 5 Hz peak was bigger than the 20 Hz peak, which made sense because I made it louder. I tried changing chunk from 256 to 1024. The peaks got sharper but also a bit noisier. I still do not fully understand that trade off, I will come back to it.

What is still unclear:
Why 50 percent overlap in Welch. I just used it because I saw it in a video. How to choose the best chunk size in real life.

Code:
day24_power_spectral_density.py, run it on Pydroid, it will show 3 plots.
VOILA!
