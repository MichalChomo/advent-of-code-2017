import sys
import math 
import numpy as np
from enum import Enum

class Direction(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def do_step(self, direction):
        if direction == Direction.RIGHT:
            self.x += 1
        elif direction == Direction.UP:
            self.y -= 1
        elif direction == Direction.LEFT:
            self.x -= 1
        elif direction == Direction.DOWN:
            self.y += 1

    def inc_all(self):
        self.x += 1
        self.y += 1

    def get_max(self):
        return max(self.x, self.y)


def change_direction(direction):
    return Direction((direction.value + 1) % 4)

def get_square_sum(coords, mat):
    total = 0
    for i in range(coords.y-1, coords.y+2):
        for j in range(coords.x-1, coords.x+2):
            if i < 0 or j < 0: continue
            try:
                total += mat[i,j]
            except:
                pass
    return total

def resize_mat(n, coords, mat):
    tmp = np.zeros((n+2, n+2), dtype=np.int)
    tmp[1:-1,1:-1] = mat
    coords.inc_all()
    return (coords, tmp)

def bounds_reached(coords, mat):
    return coords.x >= math.sqrt(mat.size) or coords.y >= math.sqrt(mat.size)

try:
    input_num = int(sys.argv[1])
except Exception as ex:
    print("usage: python day3_part2.py N")
    exit()

mat = np.matrix([[0,0,0], [0,1,0], [0,0,0]])
coords = Coords(1, 1)
steps = 1
direction = Direction.RIGHT
while mat[coords.y, coords.x] < input_num:
    for two in range(2):
        for i in range(steps):
            coords.do_step(direction)
            if bounds_reached(coords, mat):
                (coords, mat) = resize_mat(coords.get_max(), coords, mat)
            mat[coords.y, coords.x] = get_square_sum(coords, mat)
            if mat[coords.y, coords.x] >= input_num:
                print(mat[coords.y, coords.x])
                exit()
        direction = change_direction(direction)
    steps += 1
