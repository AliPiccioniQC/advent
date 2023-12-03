#!/usr/bin/env python3
import re
from collections import defaultdict

f = open("test/input", "r")

ratio = defaultdict(list)

def check(m, row, col_start, col_end, val):
    # print(f"({row}, {col_start}, {col_end})")
    for adj_row in range(max(0, row - 1), min(len(m), row + 2)):
         for adj_col in range(max(0, col_start - 1), min(len(m[0]), col_end + 1)):
            if not m[adj_row][adj_col].isnumeric() and not m[adj_row][adj_col] == ".":
                key = f"{adj_row}, {adj_col}"
                ratio[key].append(val)
                print(f"  ({key})")
                return True
    return False

m = []
for l in f:
    m.append(l.strip())

regex = re.compile("[0-9]+")
for row in range(len(m)):
    for match in regex.finditer(m[row]):
        if check(m, row, match.start(), match.end(), int(match[0])):
            print("accept", match)
        else:
            print("reject", match)


print(ratio)
ans = 0
for val in ratio.values():
    if len(val) == 1:
        continue

    mul = 1
    for v in val:
        mul *= v
    ans += mul
print(ans)
