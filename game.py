import random
import os
import time

size = os.get_terminal_size()

field = [[0 for i in range(size[0])] for i in range(size[1])]
output = [[0 for i in range(size[0])] for i in range(size[1])]
duplicate = [[0 for i in range(size[0])] for i in range(size[1])]

# patterns
patterns = {
    0: [[1, 1],
        [1, 1]], # block
    1: [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0]], #beehive
    2: [[0, 1, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 1, 0]], # loaf
    3: [[1, 1, 0],
        [1, 0, 1],
        [0, 1, 0]], # boat
    4: [[0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]], # tub
    5: [[1],
        [1],
        [1]], # blinker
    6: [[0, 1, 1, 1],
        [1, 1, 1, 0]], # toad
    7: [[1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]], # beacon
    8: [[0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]], # glider
    9: [[0, 1, 1],
        [1, 1, 0],
        [0, 1, 0]], # r-pentomino
    10: [[0, 0, 0, 0, 0, 0, 1, 0],
         [1, 1, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 1, 1, 1]], # diehard
    11: [[0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [1, 1, 0, 0, 1, 1, 1]], # acorn
    12: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] # gosper glider gun

}

def initialize(field):
    number = random.randint(4, 12)

    for i in range(number):
        n = random.randint(0, len(patterns)-1)

        if i >= number//2:
            n = random.randint(7, len(patterns)-1)

        x = random.randint(0, int(size[0]))
        y = random.randint(0, int(size[1]))

        height = len(patterns[n])
        width = len(patterns[n][0])

        for j in range(height):
            for k in range(width):

                ypos = y + j
                xpos = x + k

                if ypos > size[1] - 1:
                    ypos = j
                if xpos > size[0] - 1:
                    xpos = k

                if j > size[1] - 1:
                    ypos = 0
                if k > size[0] - 1:
                    xpos = 0

                field[ypos][xpos] = patterns[n][j][k]
                duplicate[ypos][xpos] = patterns[n][j][k]


initialize(field)

def count(field, y, x):
    neighbors = 0
    
    x1 = x + 1
    y1 = y + 1

    if x1 >= len(field[y]):
        x1 = 0
    if y1 >= len(field):
        y1 = 0
        
    cells = [field[y-1][x-1], field[y-1][x], field[y-1][x1], field[y][x-1], field[y][x1], field[y1][x-1], field[y1][x], field[y1][x1]]

    neighbors = cells.count(1)

    return neighbors

    

while True:
    output = [["#" if x == 1 else " " for x in row] for row in field]


    outlist = [''.join(str(c) for c in lst) for lst in output]
    outl = '\n'.join(outlist)

    print(outl)
    time.sleep(0.22)

    for y in range(len(field)):
        for x in range(len(field[y])):
            neighbors = count(duplicate, y, x)
            
            if neighbors == 3:
                field[y][x] = 1
            elif neighbors < 2 or neighbors > 3:
                field[y][x] = 0
            

    for y in range(len(field)):
        for x in range(len(field[y])):
            duplicate[y][x] = field[y][x]