# Question

> I have `n` elements with index `0..(n-1)`. I want to distribute the elements to `m` bins like so:
> 
> * I want to fill the bins sequentially
> * The size of the bins should be between `⌊number_of_elements / number_of_bins⌋` and `⌈number_of_elements / number_of_bins⌉`. The bigger bins should come first.
> * I want to assign the elements based on the index of the element. I can only come up with solutions with various for loops. It should be possible to use only one for loop to assign the elements to a bin and `mod` and `div` and maybe `if`-operators for this. 
> 
> Example: I have `n=7` elements and and `m=3` bins. The result should be this:
> 
>     Bin 1: 0, 1, 2 
>     Bin 2: 3, 4
>     Bin 3: 5, 6

asked Aug 7 at 11:42 by **[conscho](http://stackoverflow.com/users/3258909/conscho)** ([original](http://stackoverflow.com/questions/31876912/))

# Solution
In this repository, there are several different, disconnected branches. Each one contains a particular solution to the problem using different dependencies or approaches.
