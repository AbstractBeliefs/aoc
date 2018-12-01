from itertools import cycle

puzzle = [int(element) for element in open("1.1.dat", 'r').readlines()]

total = 0
previous = {0}

for element in cycle(puzzle):
    total += element
    if total in previous:
        print "Double:", total
        break
    previous.add(total)
