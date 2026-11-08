Day 25
Hilbert Transform and Envelope

Today I did Hilbert Transform. To be honest at first I did not really get it, but after I ran the code it made sense.

What I did was I made an AM signal. I used a small message of 5 Hz and put it inside a carrier of 50 Hz. Then I used hilbert from scipy to get the envelope.

The envelope is just the outline of the signal. When I plotted it, the red line was sitting on top of the blue signal and following it up and down. That was the envelope.

I also tried to get my message back from the envelope. I did envelope minus 1 and it looked almost the same as my original message. That was when I knew it worked.


I ran it on Pydroid. It showed two plots. First one is AM signal and envelope. Second one is original message and the one I recovered.

What I learnt from today is that we can use Hilbert to find the message inside a signal without knowing the carrier. They use this in radio and ECG and things like that.

Next I will do Day 26.
