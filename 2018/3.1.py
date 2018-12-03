import re
from collections import defaultdict

puzzle = [element.replace("\n", "") for element in open("3.1.dat", 'r').readlines()]
rectangles = [map(int, re.match("#\d+ @ (\d+),(\d+): (\d+)x(\d+)", element).groups()) for element in puzzle]

sheet = defaultdict(int)

for rect in rectangles:
    for x in range(rect[0], rect[0]+rect[2]):
        for y in range(rect[1], rect[1]+rect[3]):
            sheet[x,y] += 1

print len([sqinch for sqinch in sheet.values() if sqinch > 1])
