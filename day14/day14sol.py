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
    for b in line:
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


def exec_mem(line: str):
    loc, val = line.split(" = ")

    return

with open('test.txt') as data:
    for line in data:
        if line.startswith('mem'):
            exec_mem(line)
        elif line.startswith('mask'):
            exec_mask(line)

print("One Mask: {:b}".format(one_mask))
print("Zero Mask: {:b}".format(zero_mask))