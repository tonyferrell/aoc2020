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
    your_ticket = next(data)
    print("Your ticket:", your_ticket)

    print("Throwing awway:", next(data))
    print("Throwing awway:",next(data))

    line = next(data).strip()
    print("Spied:")

    bad = []
    while line:
        print("S:", line)
        vals = map(int, line.split(','))
        for val in vals:
            found = False
            for r_n, r in rules.items():
                for sub_r in r:
                    if sub_r(val):
                        # print("{} satisfies {}".format(val, r_n))
                        found = True
                        break
            
            if not found:
                print("{} satisfies no rules.".format(val))
                bad.append(val)


        try:
            line = next(data).strip()
        except StopIteration:
            # EOF
            break
    
print(sum(bad))
