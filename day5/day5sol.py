import math
def bin_part_f(start: int, end_index: int, forward: str, backward: str):
    def bin_part_impl(bin: str):
        s = start
        e = end_index
        # print("Doing {}".format(bin))
        while(len(bin)):
            # print("Range: ({}, {})".format(s, e))
            first, bin = bin[0], bin[1:]
            if first == forward:
                e = math.floor((s + e) / 2)
            elif first == backward:
                s = math.ceil((s + e) / 2)
        
        if s == e:
            return s
        else:
            raise Exception("Mistakes were made {}, {}".format(s, e))

    return bin_part_impl

row_partition = bin_part_f(0, 127, 'F', 'B')
col_partition = bin_part_f(0, 7, 'L', 'R')


ex = 'BBFFBBFRLL'
def get_id(i: str) -> int:
    row = row_partition(i[:7])
    col = col_partition(i[7:])

    return row * 8 + col

all_ids = []
with open('input.txt') as data:
    for row in data:
        new_id = get_id(row)
        all_ids.append(new_id)

all_ids.sort()

last = -1
for i in all_ids:
    if last != -1 and last != (i-1):
        print("({}, -{}-, {})".format(last, (i-1), i))
        last = i
    else:
        last = i
