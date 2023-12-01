#!/usr/bin/env python

# re does not support overlapping matches.
import regex

f = open("test/input", "r")

d = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
}

expr = "|".join(d.keys())
print(expr)
p = regex.compile(expr)

ans = 0
print("transform")
for l in f:
    m = p.findall(l, overlapped=True)
    val = d[m[0]] * 10 + d[m[-1]]
    #print("\n", l)
    print("  ", m)
    #print("  ", val)
    ans += val

print(ans)
