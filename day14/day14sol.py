import re

zero_mask = 0
one_mask = 0

curr_mask = ""
mem = {}
def exec_mask(line: str):
    global zero_mask, one_mask
    _, mask = line.split(' = ')
    print("This is mask", mask)
    one_mask = 0
    zero_mask = 0
    for b in mask.strip():
        one_mask = one_mask << 1
        zero_mask = zero_mask << 1

        if b == '1':
            one_mask |= 1
            zero_mask |= 1
        elif b == '0':
            one_mask |= 0
            zero_mask |= 0
        elif b == 'X':
            one_mask |= 0
            zero_mask |= 1
        else:
            raise Exception("Unexpected value: ", b)

mem_loc = re.compile("mem\[(\d+)\]")
def exec_mem(line: str):
    verbose = False
    loc, val = line.split(" = ")
    loc_str = mem_loc.match(loc)
    loc_i = int(loc_str[1])
    val_i = int(val)
    if verbose:
        print("Val: {:b}".format(val_i))
    val_i &= zero_mask
    if verbose:
        print("Val: {:b}".format(val_i))
    val_i |= one_mask
    if verbose:
        print("Val: {:b}".format(val_i))

    print("mem[{}] = {}".format(loc_i, val_i))
    mem[loc_i] = val_i

    return

with open('input.txt') as data:
    for line in data:
        if line.startswith('mem'):
            exec_mem(line)
        elif line.startswith('mask'):
            exec_mask(line)
            print("One Mask: {:b}".format(one_mask))
            print("Zero Mask: {:b}".format(zero_mask))

print("Memory Total: {}".format(sum([val for mem, val in mem.items()])))