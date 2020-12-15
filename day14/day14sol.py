import re

zero_mask = 0
one_mask = 0

curr_mask = ""
mem = {}
    
def expand_mask(mask, cum, gen_masks):
    if mask == "":
        gen_masks.append(cum)
        print("Found Mask! {:b}".format(cum))
        return []

    next_m, remain_m = mask[0], mask[1:]
    cum = cum << 1
    if next_m == '1':
        cum = cum | 1
        expand_mask(remain_m, cum, gen_masks)
        return
    elif next_m == '0':
        expand_mask(remain_m, cum, gen_masks)
        return
    elif next_m == 'X':
        expand_mask(remain_m, cum, gen_masks)
        expand_mask(remain_m, cum | 1, gen_masks)
        return
    else:
        raise Exception("Unknown Mask Char:", next_m)

def gen_one_and_zero_masks(mask):
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
    return (zero_mask, one_mask)
    
def exec_mask(line: str):
    _, mask = line.split(" = ")
    curr_mask = mask.strip()

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
a_val = 42
masks = []
expand_mask(a_mask, 0, masks)
for i in masks:
    n = a_val

    zero_mask, one_mask = gen_one_and_zero_masks('{:b}'.format(i))

    n &= zero_mask
    n |= one_mask
    print("#" * 25)
    print("     {:9b}\n     {:9b}".format(zero_mask, one_mask))
    print("val: {:9b}".format(a_val))
    print("N:   {:9b} ({})".format(n, n))