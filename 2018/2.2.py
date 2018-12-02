from itertools import combinations

puzzle = [element.replace("\n", "") for element in open("2.1.dat", 'r').readlines()]

for left, right in combinations(puzzle, 2):
    pairwise = zip(left, right)
    diffs = filter(lambda p: p[0] != p[1], pairwise)
    if len(diffs) == 1:
        print "".join(p[0] for p in pairwise if p[0] == p[1])
