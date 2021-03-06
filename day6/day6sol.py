from typing import List

base = ord('a')
def an_group(g: List[str]):
    letters = [0 for _ in range(26)]
    for person in g:
       for vote in person:
           ind = ord(vote) - base
           letters[ind] += 1

    r = map(lambda x: 1 if x == len(g) else 0, letters)

    print("Parsed {} to {}".format(g, r))
    return r

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