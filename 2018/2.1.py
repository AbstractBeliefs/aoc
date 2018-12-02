from collections import Counter

puzzle = [Counter(element) for element in open("2.1.dat", 'r').readlines()]

def makefilter(search):
    def inner(element):
        for character, count in element.iteritems():
            if count == search:
                return True
        return False
    return inner

filter2 = makefilter(2)
filter3 = makefilter(3)

count2 = len(filter(filter2, puzzle))
count3 = len(filter(filter3, puzzle))

print count2 * count3
