import re

curr_mask = ""
mem = {}
    
def expand_mask(mask, val, accum, gen_masks):
    assert len(val) == len(mask), "Mask and Value must be the same"
    if mask == "" and val == "":
        gen_masks.append(accum)
        # print("Found Mask! {:b}".format(accum))
        return
    
    next_m, remain_m = mask[0], mask[1:]
    next_v, remain_v = val[0], val[1:]

    accum = accum << 1
    if next_m == '1':
        accum = accum | 1
        expand_mask(remain_m, remain_v, accum, gen_masks)
        return
    elif next_m == '0':
        b = 1 if next_v == '1' else 0
        expand_mask(remain_m, remain_v, accum | b, gen_masks)
        return
    elif next_m == 'X':
        expand_mask(remain_m, remain_v, accum, gen_masks)
        expand_mask(remain_m, remain_v, accum | 1, gen_masks)
        return
    else:
        raise Exception("Unknown Mask Char:", next_m)

def exec_mask(line: str, verbose = False):
    global curr_mask

    _, mask = line.split(" = ")
    curr_mask = mask.strip()
    if verbose:
        print("Curr Mask: {}".format(curr_mask))

def apply_mask(curr_mask: str, loc_v:int):
    loc_bin = "{:b}".format(loc_v)
    needed_length = max(len(curr_mask), len(loc_bin))
    curr_mask = curr_mask.rjust(needed_length, '0')
    loc_bin = loc_bin.rjust(needed_length, '0')

    masks = []

    expand_mask(curr_mask, loc_bin, 0, masks)
    return masks

mem_loc = re.compile("mem\[(\d+)\]")
def exec_mem(line: str, verbose = False):
    loc, val = line.split(" = ")
    val_i = int(val)

    loc_str = mem_loc.match(loc)
    loc_i = int(loc_str[1])


    mem_locs = apply_mask(curr_mask, loc_i)
    for loc in mem_locs:
        if verbose:
            print("mem[{}] = {}".format(loc, val_i))
        mem[loc] = val_i

    return

with open('input.txt') as data:
    for line in data:
        verbose = False
        if line.startswith('mem'):
            exec_mem(line, verbose)
        elif line.startswith('mask'):
            exec_mask(line, verbose)

print("Memory Total: {}".format(sum([val for _, val in mem.items()])))