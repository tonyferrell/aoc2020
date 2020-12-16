from functools import reduce
rules = {}

def in_range(start, end):
    def pred(x):
        return start <= x and x <= end
    
    return pred

def in_range_arr(range_arr):
    assert len(range_arr) == 2, "Range Array must be length 2"
    return in_range(int(range_arr[0]), int(range_arr[1]))

with open('input.txt') as data:
    line = next(data).strip()
    print("Rules")
    while line:
        print("Rule:", line)
        name, rule = line.split(': ')
        ranges = [x.split('-') for x in rule.split(' or ')]
        rules[name] = list(map(in_range_arr, ranges))

        line = next(data).strip()
    
    # Throw away "your ticket"
    print("Throwing awway:", next(data))
    your_ticket = next(data).strip().split(',')
    print("Your ticket:", your_ticket)

    print("Throwing awway:", next(data))
    print("Throwing awway:",next(data))

    line = next(data).strip()
    print("Spied:")

    good = []
    while line:
        # print("S:", line)
        # Parse the line
        vals = list(map(int, line.split(',')))
        # Make sure we can satisfy all rules
        row_valid = True
        for val in vals:
            # Make sure there's a rule this value satisfies.
            valid_value = False
            for r_n, r in rules.items():
                # print("Applying Rules", r_n)
                for sub_r in r:
                    if sub_r(val):
                        # print("{} satisfies {}".format(val, r_n))
                        valid_value = True
                        break
                
                # Don't look for more rules
                if valid_value:
                    # print("{} is valid".format(val))
                    break
            
            if not valid_value:
                # print("The invalid we need right now", val)
                row_valid = False
            
        if row_valid:
            print("Row {} is valid".format(vals))
            good.append(vals)
        else:
            print("Row {} is INVALID".format(vals))

        try:
            line = next(data).strip()
        except StopIteration:
            # EOF
            break

def any_subrule(val, list_rules):
    for f in list_rules:
        if f(val):
            return True

    return False

possible = []

ct = len(good[0])
rows = good
sats = {}
poss = {}
for rn, rule_list in rules.items():
    for i in range(ct):
        # Check if each row satisfies this rule
        valid_for_this_i = True
        for r in rows:
            val_to_check = r[i]
            valid_for_this_i = any_subrule(val_to_check, rule_list)

            if not valid_for_this_i:
                break

        if valid_for_this_i:
            if not i in sats:
                sats[i] = []
            if not rn in poss:
                poss[rn] = []

            sats[i].append(rn)
            poss[rn].append(i)
print()
print("one")
print(sats)
print()
print("two")
print(poss)

solution = [""] * ct
solved = 0
found = []
found_i = []
while solved < ct:
    new_sats = {}
    for k, v in sats.items():
        if k in found_i:
            continue

        for f in found:
            if f in v:
                v.remove(f)

        new_sats[k] = v
    
    sats = new_sats
    found = []
    found_i = []
            
    for i, poss in sats.items():
        if len(poss) == 1:
            print("Solved: {} == {}".format(i, poss))
            solution[i] = poss[0]
            solved += 1

            found.append(poss[0])

print(solution)
mult = 1
for i, s in enumerate(solution):
    if s.startswith("departure"):
        mult *= int(your_ticket[i])

print(mult)
