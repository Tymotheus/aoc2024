Solution on lists does not perform in reasonable time for n=25.
Probably it does not complete in time shorter than 1hour.
Running cProfiler indicates that insert and pop operations take a lot of time
(makes sense, they require full list recopying)
Implemented a linked list, reduced the timing to <0.5s.
This solution goes instantly for n=25 and very first for n<30.
It is however to slow for n = 75.