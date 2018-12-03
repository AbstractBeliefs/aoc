import re
from itertools import combinations

puzzle = [element.replace("\n", "") for element in open("3.1.dat", 'r').readlines()]
rectangles = [map(int, re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", element).groups()) for element in puzzle]
rectangles = [
        {
            "id": r[0],
            "left": r[1],
            "top": r[2],
            "right": r[1]+r[3],
            "bottom": r[2]+r[4],
            "intersect": False
        } for r in rectangles]


def intersection(a, b):
    if a["bottom"] < b["top"] or \
       b["bottom"] < a["top"] or \
       a["right"] < b["left"] or \
       b["right"] < a["left"]:
        return False
    else:
        return True

for a, b in combinations(rectangles, 2):
    if intersection(a, b):
        a["intersect"] = True
        b["intersect"] = True

for r in rectangles:
    if r["intersect"] is False:
        print r["id"]
