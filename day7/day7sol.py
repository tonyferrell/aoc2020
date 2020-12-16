import re
all_outer = {"shiny gold bag" : 1}

no_count = re.compile("(\d+\s)?(\D+ bag)s?\W*")

bags = {}
def clean_bag(bag, count = False):
    bag = bag.strip()
    m = no_count.match(bag)
    if no_count:
        if not count:
            return m.group(2)
        else:
            count = int(m.group(1)) if m.group(1) is not None else 0
            return m.group(2), count
    else:
        return bag

with open('input.txt') as data:
    for line in data:
        outer, inner = line.split(" contain ")
        ib = inner.split(', ')
        bags[clean_bag(outer)] = list(map(lambda x: clean_bag(x, count=True), ib))

def can_hold(needle, haystack, top):
    print("Looking for", needle)
    if needle in haystack:
        contained_by = haystack.pop(needle)
        for n1 in contained_by:
            if not n1 in top:
                top[n1] = 0
            top[n1] += 1
            can_hold(n1, haystack, top)

# for b, c in bags.items():
#     print("{} => {}".format(b,c))

seen = {}
def must_hold(bag, rules, idet = 0):
    verbose = True
    left = idet * "-"
    if bag in seen:
        if verbose:
            print(left + "Cached {} == {}!".format(bag, seen[bag]))
        return seen[bag]

    if not bag in rules: # Should only be "no other"
        # if verbose:
            # print(left + "{} contains nothing x 1".format(bag))
        return 0
    else:
        # Figure out how many this bag contains
        in_this_bag = 0

        for b, count in rules[bag]:
            if verbose:
                print(left + "{} contains {} x {}".format(bag, b, count))

            bags_in_child = must_hold(b, rules, idet + 4)
            this_contains = (count * bags_in_child) + count 
            seen[b] = bags_in_child

            in_this_bag += this_contains
            if verbose:
                print(left + "{} contains {} * {} = {} bags".format(bag, count, bags_in_child, this_contains))
            
        return in_this_bag

print("Res: {}".format(must_hold('shiny gold bag', bags)))
for k, v in seen.items():
    print(k, "==>", v)
