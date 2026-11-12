DAY 29 - FILTER COMPARISON PROJECT:
WHAT I DID TODAY:
I Compared FIR And IIR On The Same Signal. I Wanted To See Which One Really Wins. I Used The Same Signal From Day 17 And Day 18. 5Hz Clean Plus 50Hz Noise. Cutoff 15Hz. Same Signal For All Filters, So The Comparison Is Fair.
THE FILTERS I COMPARED:
1. FIR, Moving Average With 20 Taps. This Is From Day 17.
2. IIR 1st Order. This Is From Day 18. I Used The Alpha Formula.
3. IIR 2nd Order. This Is Also From Day 18. I Used The b0, b1, b2, a1, a2 Numbers I Got From An Online Calculator.

MY RESULT:
No Filter: Error 0.5657
FIR 20 Taps: Error 0.0549
IIR 1st Order: Error 0.2589
IIR 2nd Order: Error 0.4069
I Expected IIR 2nd Order To Win. It Did Not. FIR Won.

WHAT I LEARNED:
I Made A Mistake On Day 18 And I Found It Today. Those 2nd Order Numbers Were Not For fs Equals 500. I Just Copied Them From The Calculator.
That Is Why The IIR 2nd Order Plot Still Has Ripple.
I Also Saw That IIR Has Delay. You Can See It In The Plot. The Purple Line Is Shifted A Little. FIR With mode Equals same Does Not Shift Like That. So For Today, FIR Wins For Me. Not Because FIR Is Always Better. Because I Used Wrong Numbers For IIR. I Will Fix The IIR Numbers Properly On Day 

MY PLOT:
The First Plot Is Original. The Second Is FIR. The Third Is IIR 1st Order. The Fourth Is IIR 2nd Order. The Black Dashed Line Is The Clean 5Hz Signal I Wanted Back.
