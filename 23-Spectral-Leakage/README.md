DAY 23 - WHEN FFT LIES: LEAKAGE, HANN WINDOW, ZERO PADDING & RESOLUTION:

Today was one of those days where FFT started to make sense and then confuse me again.

I thought FFT just shows you the frequency. It does, but only if your signal fits perfectly in the window. If it doesn't, everything leaks everywhere.

WHAT I DID:

fs = 100Hz for everything.

First I tested a 10Hz sine with N=100. That one is clean because 10Hz fits exactly in 1 second. One peak, nothing else.

Then I tested 10.5Hz with the same N=100. That one does NOT fit. 10.5 cycles in 1 second, so the start and end don't match. FFT thinks there is a jump, so it spreads energy to all the other bins. That's leakage.

I was like, okay so how do we fix it?

HANN WINDOW:

I tried the Hann window. Basically it just fades the start and end to zero so FFT doesn't see the jump.

It works. The side lobes dropped a lot. The peak is still at 10-11Hz but everything else is almost gone.

Before Hann the side stuff was around 3, after Hann it was like 0.01. Big difference.

Downside is the peak gets a bit wider and smaller. That's the tradeoff.

ZERO PADDING:

Then I tried zero padding to 1024. I thought this would help resolution lol it doesnt.

It just makes the plot look smooth. Same info, just more points in between. It doesn't actually let you see two close frequencies better. I kept thinking it would, it doesn't.

RESOLUTION - N=100 VS N=1000:

This was the last test and the one that finally clicked.

I made a signal with 10Hz + 12Hz together.

 With N=100 (1 second), I cant separate them. They just merge into one fat peak. Resolution is 1Hz but Hann makes each peak like 4Hz wide, so 10 and 12 crash into each other.

 With N=1000 (10 seconds), I can actually see two separate peaks. One at 10, one at 12. Resolution is 0.1Hz now, so there is space.

So more samples = longer signal = sharper peaks = you can tell close frequencies apart. That's it.

FILES IN THIS FOLDER:

- day23_spectral_leakage.py / day23_spectral_leakage.png - 10Hz vs 10.5Hz, this is where leakage shows
- day23_hann_windows_zero... - Hann vs no window, side by side
- day23_zero_padding_looks... - No padding vs padded to 1024
- day23_spectral_leakage_res... - 10Hz + 12Hz with N=100 and N=1000

HOW TO RUN:

I ran all of this on Pydroid on my phone.

Just open any .py file and run it. The plot will pop up. Tap the save icon at the bottom to save the png.

WHAT I LEARNT:

- Leakage happens when the signal doesn't fit in the window
- Hann window fixes leakage but makes peaks wider
- Zero padding does NOT improve real resolution, it just interpolates
- Real resolution comes from longer signals (bigger N)
