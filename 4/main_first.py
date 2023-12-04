#!/usr/bin/env python

import re

f = open("test/input", "r")


ans = 0
card_re = re.compile("Card.*:(.*)\|(.*)\n")
for l in f:
    print(l.strip())
    card = card_re.findall(l)
    expr = "\\b" + "\\b|\\b".join(card[0][0].strip().split()) + "\\b"
    print("  regex:", expr)
    search_re = re.compile(expr)
    found = search_re.findall(card[0][1].strip())
    print("  matches:", found)
    if len(found) > 0:
        ans += pow(2, len(found) - 1)

print(ans)
