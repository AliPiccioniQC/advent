#!/usr/bin/env python

import re
from collections import defaultdict

f = open("test/input", "r")


ans = 0
card_re = re.compile("Card.*:(.*)\|(.*)\n")
card_count = defaultdict(int)
i = 1
for l in f:
    ans += card_count[i] + 1
    print(l.strip())
    card = card_re.findall(l)
    expr = "\\b" + "\\b|\\b".join(card[0][0].strip().split()) + "\\b"
    print("  regex:", expr)
    search_re = re.compile(expr)
    found = search_re.findall(card[0][1].strip())
    print("  matches:", found)
    for j in range(i + 1, i + 1 + len(found)):
        card_count[j] += card_count[i] + 1
        print(f"  {j} -> {card_count[i] + 1}")

    i += 1

print(ans)
