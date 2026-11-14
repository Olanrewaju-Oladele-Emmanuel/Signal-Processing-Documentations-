My 30 Days of Learning Signal Processing

By Olanrewaju Oladele Emmanuel

I did all of this on my phone. I did not have a laptop at all. I used only Pydroid 3 and a small amount of data. Some days my phone would just hang and I had to start again.

I started because I wanted to really understand signals. I did not want to just copy code from somewhere. I wanted to know why a radio works, why noise spoils a signal, and how we can clean it again.

So I gave myself 30 days. One day, one topic, one plot. Some days were easy and some days were difficult. But I finished it.

I used Python, Pydroid 3, NumPy, SciPy, and Matplotlib. That was all.

Let me explain how it went.

Day 1: Sine wave. I just wanted to see how a wave looks.
Day 2: Cosine wave. I realised it is the same as a sine wave, just shifted.
Day 3: Frequency effect. I changed the frequency and saw the wave become faster or slower.
Day 4: Amplitude. I changed the height and the wave became taller or shorter.
Day 5: Phase shift. I shifted it left and right. It was still the same wave, but it started from a different place.
Day 6: Superposition. I added two waves together and got a new wave. I really liked that one.

Day 7: Fourier series. This felt like magic. You can build a big wave from small sine waves.
Day 8: Fourier transform. This was where I moved from the time side to the frequency side.
Day 9: IFFT filter. This was the reverse. From frequency back to time.
Day 10: Windowing. I learned that if you do not use a window, your FFT can mislead you.

Day 11: Convolution. At first I did not understand it. Later I saw that it is just filtering.
Day 12: STFT. This one shows frequency as time moves. It is not just one picture.
Day 13: Correlation. This is for checking if two signals look alike.
Day 14: Impulse. One small knock, and you see what the system will do.
Day 15: Sampling theorem. If you sample too slowly, you will lose your signal.
Day 16: Aliasing. This is the problem that happens when you sample too slowly. Your signal turns into something else.

Day 17: FIR filter design. This was my first real FIR filter. I was very happy.
Day 18: IIR filter design. This one uses fewer taps, but it was a little more confusing.
Day 19: High pass band pass filter. This is for allowing only some frequencies to pass.

Day 20: AM modulation. You put a small message on top of a big carrier.
Day 21: FM modulation. It is the same idea, but with FM. AM was easier for me.
Day 22: Noisy SNR. I added noise, then I measured how bad it was.
Day 23: Spectral leakage. This is why FFT sometimes shows things that are not really there.
Day 24: Power spectral density. This shows how power spreads across frequencies.
Day 25: Hilbert transform and envelope. This one helped me find the envelope of a signal.

Day 26: Signal reconstruction. Building a signal back from samples.
Day 27: Wavelet transform. Another way to see time and frequency together.
Day 28: ECG audio analysis. This one used real signals, not just sine waves. ECG and audio. It made everything feel real for me.
Day 29: Filter comparison. I compared all the filters I built, to see which one was better and which one was worse.

Day 30 was the last one. It was my favourite.

I put everything together. Original, then add noise, then filter, then modulate, then demodulate, then recover.

My code for day 30 in plain words:
msg equals sin of 2 times pi times 5 times t
noisy equals msg plus 0.6 times sin of 2 times pi times 50 times t plus 0.2 times random noise
fir equals firwin with 51 taps, 20 cutoff, fs, Hamming window
filtered equals lfilter with fir and noisy
modulated equals 1 plus 0.8 times filtered, all times carrier
envelope equals absolute value of Hilbert of modulated
recovered equals envelope minus mean of envelope

Settings I used:
Message: 5Hz sine wave
Sampling: 1000Hz
Noise: 50Hz plus random
Filter: FIR, 51 taps, 20Hz cutoff
Carrier: 100Hz
Modulation: 0.8

Result:
Image: 30 Signal Chain slash day30 signal chain.png

Top to bottom:
1. Original, my clean signal
2. Noisy, after I spoiled it with noise
3. Filtered, after FIR cleaned it
4. Recovered, purple is recovered, blue dashed is original

They almost overlap. When I saw it, I was very happy. After 30 days, I could send a signal through noise and still get it back. It worked.

How to run it:
pip install numpy matplotlib scipy
python day30.py

I ran everything on Pydroid 3 on Android, so it should run anywhere Python runs.

What I learned from all this:
A system is a chain. If one part fails, everything fails. You can have a perfect filter but a bad demodulator, and you will still get nothing. That lesson stayed with me.

I also learned that I can learn a hard thing even without a laptop. I just need to do a little every day.

What I want to do next:
Real audio signals, not just sine waves
Digital filters and Z transform properly
Then software engineering, how to turn all this into real products
Later, satellite and RF work. That is the dream.

Thank you for checking my repo. If you are also learning on your phone like me, you can do it too.

Emmanuel
