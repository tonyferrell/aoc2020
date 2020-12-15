import re
all_outer = {"shiny gold bag" : 1}

no_count = re.compile("(\d+\s)?(\D+ bag)s?\W*")

bags = {}
def clean_bag(bag):
    bag = bag.strip()
    m = no_count.match(bag)
    if no_count:
        return m.group(2)
    else:
        return bag

with open('input.txt') as data:
    for line in data:
        outer, inner = line.split(" contain ")
        ib = inner.split(', ')
        bags[clean_bag(outer)] = list(map(clean_bag, ib))

who_holds = {}
for type, c in bags.items():
    for b in c:
        if not b in who_holds:
            who_holds[b] = []

        who_holds[b] += [type]

for child, parent in who_holds.items():
    print("'{}' <- {}".format(child, parent))

def can_hold(needle, haystack, top):
    print("Looking for", needle)
    if needle in haystack:
        contained_by = haystack.pop(needle)
        for n1 in contained_by:
            if not n1 in top:
                top[n1] = 0
            top[n1] += 1
            can_hold(n1, haystack, top)

top = {}
can_hold('shiny gold bag', who_holds, top)
for k in top:
    print(k)
print(len(top))
