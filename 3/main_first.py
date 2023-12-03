#!/usr/bin/env python3
import re

f = open("test/input", "r")

def check(m, row, col_start, col_end):
    # print(f"({row}, {col_start}, {col_end})")
    for adj_row in range(max(0, row - 1), min(len(m), row + 2)):
         for adj_col in range(max(0, col_start - 1), min(len(m[0]), col_end + 1)):
            if not m[adj_row][adj_col].isnumeric() and not m[adj_row][adj_col] == ".":
                 print(f"  ({adj_row}, {adj_col})")
                 return True
    return False

m = []
for l in f:
    m.append(l.strip())

regex = re.compile("[0-9]+")
ans = 0
for row in range(len(m)):
    for match in regex.finditer(m[row]):
        if check(m, row, match.start(), match.end()):
            print("accept", match)
            ans += int(match[0])
        else:
            print("reject", match)


print(ans)
