DAY 28 
ECG AND AUDIO

This is day 28 of my signal processing journey.

WHAT I DID

I made a fake ecg signal at 72 bpm because I dont have a sensor.
Then I added noise to it like in real life, baseline wander, muscle noise, 50hz power noise.

I tried to clean it with a simple moving average filter.
Then I tried to find the R-peaks and calculate heart rate and HRV.

For the audio part, I made a chirp that goes from 200hz to 800hz.
Then I did STFT by hand like we did on day 12 and plotted the spectrogram.


WHAT I GOT

Beats found: 12
Heart rate: 72.0 bpm
Avg RR: 833 ms
HRV: around 5-10 ms

The spectrogram shows a yellow line going up. That means frequency is increasing, so the STFT worked.

WHAT WAS HARD

The filtering part was confusing at first. My peaks were not detected because my threshold was too high.
I lowered it to 0.6 times max and added a min distance so it doesn't pick the same peak twice.

Also the spectrogram axes were wrong at first. I fixed it to show Hz and seconds instead of bins.

WHAT I LEARNED

How to clean a real world signal with just moving average
How to find peaks without scipy
How STFT actually works, not just theory
How to go from time domain to time-frequency

NEXT

Day 29 
