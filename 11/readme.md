Solution on lists does not perform in reasonable time for n=25.
Probably it does not complete in time shorter than 1hour.
Running cProfiler indicates that insert and pop operations take a lot of time
(makes sense, they require full list recopying)
Implemented a linked list, reduced the timing to <0.5s.
This solution goes instantly for n=25 and very first for n<30.
It is however too slow for n = 75.

Attempt number 2 is to instead reduce the length of the list.
We ultimately just care about the length of the list, not its content.
It is also full deterministic and no 2 elements are combined, it is just gradual decay of elements.
Caching might be used, especially that numerous times it will happen that we will be processing 0's element
with their deterministic path forward.
There are also a lot of elements 2,4,6,8.

Using profiler, for linked lists and no caching, on my macbook the job for 30 epochs and final data runs for 3.4 seconds.