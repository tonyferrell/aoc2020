import re

zero_mask = 0
one_mask = 0

curr_mask = ""
mem = {}
class Maskalicious:
    def __init__(self, val, children = []):
        self.val = val
        self.children = children
    
def expand_mask(mask, cum, gen_masks):
    if mask == "":
        gen_masks.append(cum)
        print("Found Mask! {:b}".format(cum))
        return []

    next_m, remain_m = mask[0], mask[1:]
    cum = cum << 1
    if next_m == '1':
        cum = cum | 1
        return [Maskalicious(cum, expand_mask(remain_m, cum, gen_masks))]
    elif next_m == '0':
        return [Maskalicious(cum, expand_mask(remain_m, cum, gen_masks))]
    elif next_m == 'X':
        return [Maskalicious(cum, [expand_mask(remain_m, cum, gen_masks), Maskalicious(cum | 1, expand_mask(remain_m, cum | 1, gen_masks))])]
    else:
        raise Exception("Unknown Mask Char:", next_m)

def exec_mask(line: str):
    global zero_mask, one_mask, curr_mask
    _, mask = line.split(' = ')
    one_mask = 0
    zero_mask = 0
    curr_mask = mask.strip()
    for b in curr_mask:
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

with open('test2.txt') as data:
    for line in data:
        if line.startswith('mem'):
            exec_mem(line)
        elif line.startswith('mask'):
            exec_mask(line)
            print("Curr Mask: {}".format(curr_mask))
            print("One  Mask: {:b}".format(one_mask))
            print("Zero Mask: {:b}".format(zero_mask))

print("Memory Total: {}".format(sum([val for mem, val in mem.items()])))
a_mask = "000000000000000000000000000000X1001X"
a_val = "{:b}".format(42)
masks = []
expand_mask(a_mask, 0, masks)
for i in masks:
    print('Eeep: {:b}'.format(i))