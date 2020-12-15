from os import curdir
from typing import List
from functools import reduce
import numpy as np

inst = []
with open('input.txt') as data:
    inst = [(x[0], int(x[1:-1])) for x in data.readlines()]

xy = [0, 0]
wp = [10, 1]
card_dirs = ['N', 'E', 'S', 'W']
dirs = [
        [0, 1], # 'N'
        [1, 0], # 'E'
        [0, -1],# 'S'
        [-1, 0],# 'W'
]

lookup = dict(zip(card_dirs, dirs))

def scale(dir, amt):
    return [x * amt for x in dir]

def comb(x, y):
    return [a + b for a, b in zip(x, y)]

def get_dir(curr_dir: List[int], cmd: str, i: int):
    mult = (-1 if cmd == 'L' else 1)
    steps = mult * int(i / 90)
    new = np.rot90([[curr_dir[0], curr_dir[1]], [-curr_dir[1], -curr_dir[0]]], steps)
    print("New:", new[0])
    curr_dir = new[0]
    return curr_dir


def fmt(s):
    i = dirs.index(s)
    return card_dirs[i]

for cmd, amt in inst:
    if cmd in ['R', 'L']:
        wp = get_dir(wp, cmd, amt)
    elif cmd == 'F':
        mv = scale(wp, amt)
        xy = comb(xy, mv)
    else:
        # Just a raw wp move
        mv = scale(lookup[cmd], amt)
        wp = comb(wp, mv)

    # Also move
    print("After {}{} move *** WP: {}, Ship: {}".format(cmd, amt, wp, xy))

print(reduce(lambda x,y: abs(x) + abs(y), xy))