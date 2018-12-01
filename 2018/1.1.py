puzzle = [int(element) for element in open("1.1.dat", 'r').readlines()]

total = sum(element for element in puzzle)
print total
