Day 27 
Wavelet

Today I tried wavelet transform.

I have been using FFT for a while now, and FFT is good but it has one problem.
It tells you what frequency is in the signal, but it does not tell you when it happened.

So I wanted to see if wavelet can do better.

What I did

I made a signal myself. First half is 5Hz, second half is 20Hz.
Then I added a spike at 0.75s, just to make it interesting.

After that I did a moving average. That gave me the smooth part.
Then I did original minus smooth, that gave me the sharp part where the spike is.

Then I did the CWT with a Morlet wavelet. Scales 4, 8, 16, 32.

File is day27_wavelet_transform.py

To run it:
python day27_wavelet_transform.py

What I saw

The first plot is the signal. You can see it change at 0.5s, and the spike at 0.75s.

Second plot is the smooth part. Spike is almost gone there.

Third plot is the detail. Spike is very clear there.

Fourth plot is the scalogram. You can see when the frequency changes, and you can see a bright line where the spike is.

So yeah, wavelet shows both time and frequency. That is the whole point.

