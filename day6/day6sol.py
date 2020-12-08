from typing import List

base = ord('a')
def an_group(g: List[str]):
    letters = [0 for _ in range(26)]
    for person in g:
       for vote in person:
           ind = ord(vote) - base
           letters[ind] = 1

    print("Parsed {} to {}".format(g, letters))
    return letters

def part1():
    count = 0
    group = []

    with open('input.txt') as data:
        for line in data:
            line = line.strip()
            print("Parsing", line)
            if line == "":
                # End of a group
                count += sum(an_group(group))
                group = []
            else:
                group.append(line)

    print("Total {}".format(count))


part1()