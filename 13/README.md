For part two:
Conversion to int64 was needed, int32 cant handle such big values.
Also I tuned the rtol and atol lazily.
Not calculating it as I should, but by increasing rtol until the example solution will yield that prizes 2 and 4 are reachable :)
