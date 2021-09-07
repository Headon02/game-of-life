import random
import os
import time

size = os.get_terminal_size()

field = [[" " for i in range(size[0])] for i in range(size[1])]
duplicate = [[" " for i in range(size[0])] for i in range(size[1])]

# patterns
patterns = {
    0: [["#", "#"],
        ["#", "#"]], # block
    1: [[" ", "#", "#", " "],
        ["#", " ", " ", "#"],
        [" ", "#", "#", " "]], #beehive
    2: [[" ", "#", "#", " "],
        ["#", " ", " ", "#"],
        [" ", "#", " ", "#"],
        [" ", " ", "#", " "]], # loaf
    3: [["#", "#", " "],
        ["#", " ", "#"],
        [" ", "#", " "]], # boat
    4: [[" ", "#", " "],
        ["#", " ", "#"],
        [" ", "#", " "]], # tub
    5: [["#"],
        ["#"],
        ["#"]], # blinker
    6: [[" ", "#", "#", "#"],
        ["#", "#", "#", " "]], # toad
    7: [["#", "#", " ", " "],
        ["#", "#", " ", " "],
        [" ", " ", "#", "#"],
        [" ", " ", "#", "#"]], # beacon
    8: [[" ", "#", " "],
        [" ", " ", "#"],
        ["#", "#", "#"]], # glider
    9: [[" ", "#", "#"],
        ["#", "#", " "],
        [" ", "#", " "]], # r-pentomino
    10: [[" ", " ", " ", " ", " ", " ", "#", " "],
         ["#", "#", " ", " ", " ", " ", " ", " "],
         [" ", "#", " ", " ", " ", "#", "#", "#"]], # diehard
    11: [[" ", "#", " ", " ", " ", " ", " "],
         [" ", " ", " ", "#", " ", " ", " "],
         ["#", "#", " ", " ", "#", "#", "#"]], # acorn
    12: [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#"],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#"],
         ["#", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         ["#", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", "#", "#", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]] # gosper glider gun

}

def ask(question, yesfunc=None, nofunc=None, *args):
    while True:
        answer = input(question)
        answer = answer.lower()
        print("\n")
        
        if answer == "yes" or answer == "y":
            
            if yesfunc:
                return yesfunc(*args)
                
            break
        elif answer == "no" or answer == "n":
            
            if nofunc:
                return nofunc(*args)
                
            break

def question(question, lower, upper):
    answer = input(question)
    
    while True:
        if answer.isdecimal():
            answer = int(answer)
            
            print("\n")
            if answer >= lower and answer <= upper:
                return answer
            
        answer = input(question)
        
def position(pattern, y, x):
    
    height = len(pattern)
    width = len(pattern[0])

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

            field[ypos][xpos] = pattern[j][k]
            duplicate[ypos][xpos] = pattern[j][k]

def horiflip(p):
    return [row[::-1] for row in p]
    
def vertiflip(p):
    return p[::-1]
    
def randinit():
    number = random.randint(4, 12)

    for i in range(number):
        n = random.randint(0, len(patterns)-1)

        x = random.randint(0, int(size[0]))
        y = random.randint(0, int(size[1]))
        
        orientx = random.randint(0, 1)
        orienty = random.randint(0, 1)
        
        pattern = patterns[n]

        if orientx:
            pattern = horiflip(pattern)

        if orienty:
            pattern = vertiflip(pattern)

        position(pattern, y, x)

def place():
    for pattern in patterns:
        patt = [''.join(str(c) for c in lst) for lst in patterns[pattern]]
        p = '\n'.join(patt)
        print(pattern + 1, "\n", end = "")
        print(p, "\n")
    
    choice = question("Which pattern would you like to use?\n", 1, 13)
    
    selection = patterns[choice-1]
    selection = ask("Would you like to flip it horizontally?(y/n)\n", horiflip, lambda x: x, selection)
    selection = ask("Would you like to flip it vertically?(y/n)\n", vertiflip, lambda x: x, selection)
    
    print("The pattern:")
    patt = [''.join(str(c) for c in lst) for lst in selection]
    p = '\n'.join(patt)
    print(p)
    print("\n")
    
    x = question(f"Where would you like to place it on the x-axis, between 0 and {size[0]}?\n", 0, size[0])
    y = question(f"Where would you like to place it on the y-axis, between 0 and {size[1]}?\n", 0, size[1])
    
    position(selection, y, x)
    
    cont = ask("Would you like to add another?\n", inputmode, None)

def draw():
    print("Type the pattern you want. Use # for live cells and [space] for dead cells. Enter for new line.\n")
    drawing = []
    while True:
        row = input()
        
        if row:
            drawing.append(row)
            
        else:
            break
        
    drawing = [[ch for ch in row] for row in drawing]
    
    maxlen = len(drawing[0])
    for row in drawing:
        if len(row) > maxlen:
            maxlen = len(row)
    
    for row in drawing:
        for i in range(maxlen-len(row)):
            row.append(" ")
            
    
    x = question(f"Where would you like to place it on the x-axis, between 0 and {size[0]}?\n", 0, size[0])
    y = question(f"Where would you like to place it on the y-axis, between 0 and {size[1]}?\n", 0, size[1])
    
    position(drawing, y, x)

    cont = ask("Would you like to add another?\n", inputmode, None)
    
def inputmode():
    
    ask("Would you like to position built-in patterns? [Answer no to draw your own patterns] (y/n)\n", place, draw)
    
def conditions():
    
    print("Welcome to Conway's Game of Life.")

    ask("Would you like to input starting conditions?(y/n)\n", inputmode, randinit)
    
conditions()

def count(field, y, x):
    neighbors = 0
    
    x1 = x + 1
    y1 = y + 1

    if x1 >= len(field[y]):
        x1 = 0
    if y1 >= len(field):
        y1 = 0
        
    cells = [field[y-1][x-1], field[y-1][x], field[y-1][x1], field[y][x-1], field[y][x1], field[y1][x-1], field[y1][x], field[y1][x1]]

    neighbors = cells.count("#")

    return neighbors

    

while True:

    outlist = [''.join(str(c) for c in lst) for lst in field]
    outl = '\n'.join(outlist)

    print(outl)
    time.sleep(0.22)

    for y in range(len(field)):
        for x in range(len(field[y])):
            neighbors = count(duplicate, y, x)
            
            if neighbors == 3:
                field[y][x] = "#"
            elif neighbors < 2 or neighbors > 3:
                field[y][x] = " "
            

    for y in range(len(field)):
        for x in range(len(field[y])):
            duplicate[y][x] = field[y][x]