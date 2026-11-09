 Day 26 
Signal Reconstruction

Today I did signal reconstruction. The idea is simple, if we sample a signal well, we can get the full signal back.

What I did was I made a 5 Hz sine wave first. Then I sampled it at 50 Hz. I picked 50 because Nyquist says we need more than 2 times the signal frequency, and 50 is more than 10, so it should be enough.

After that I used sine cardinal interpolation to rebuild the signal. Each sample makes a sinc shape and when I added them all together I got my signal back.

File: day26_signal_reconstruction.py

To run it I just did:
python day26_signal_reconstruction.py

I ran it on Pydroid and I got two plots. First one shows my original signal and the samples I took. Second one shows original and reconstructed together. They matched almost perfectly, except small error at the start.

What I learnt today is that sampling is not the end. If we sample fast enough we do not lose anything, we can reconstruct. But if we sample too slow we lose the signal and no matter what we do we cannot bring it back. That is why Nyquist matters.

Next I will do Day 27.
