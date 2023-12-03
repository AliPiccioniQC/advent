#!/usr/bin/env python

f = open('test/input', "r")

d = {
        "red": 12,
        "green": 13,
        "blue": 14,
}

i = 1
ans = 0
for l in f:
    min_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    x = l.split(": ")
    game_id = x[0]
    game_run = x[1]
    game_steps = game_run.split(";")
    for step in game_steps:
        hands = step.split(", ")
        for hand in hands:
            num_color = hand.strip().split(" ")
            num = int(num_color[0].strip())
            color = num_color[1].strip()
            if min_cubes[color] < num:
                min_cubes[color] = num
    power = 1
    for val in min_cubes.values():
        power *= val
    ans += power
    print(power)


print(ans)
