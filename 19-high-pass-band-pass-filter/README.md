Day 19: High Pass and Band Pass Filter

For day 19 I worked on high pass and band pass filters.

I created a test signal by adding three different frequencies together, which are ten hertz, eighty hertz and two hundred hertz. That is the first plot, and that is why it looks rough and scattered.

After that I applied two filters on the same signal.

First filter is high pass filter at fifty hertz. It removes everything below fifty hertz, so ten hertz was removed. You can see the result in the second plot in red color.

Second filter is band pass filter from sixty hertz to one hundred and twenty hertz. It keeps only the frequencies inside that range, so only eighty hertz remained. The third plot in green color is now clean because only one frequency is left.

I used butter and lfilter from scipy dot signal and the sampling frequency is one thousand.

I plotted all three signals in one figure so it is easy to compare them. The image is saved as day nineteen high pass band pass filter.

That is all for day nineteen.
