Day 09 - IFFT and Filtering

Today I was trying to understand how to get a signal back after FFT.

I made a test signal: 5Hz sine wave plus 50Hz noise (to mimic powerline noise). 
In time domain it looked messy.

I did FFT and saw two clear peaks at 5Hz and 50Hz. 
Then I set the 50Hz part to zero in the FFT array and did IFFT.

After IFFT, the signal became clean 5Hz again.

This was interesting because this is how noise cancellation works - 
go to frequency domain, remove what you don't want, come back.

Code is in Day09_ifft_filter.py
Plot is day09_ifft_filter.png

Still learning, Day 9 of 30.
- Emmanuel
