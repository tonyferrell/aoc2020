from typing import List

# Read the data
window = 5
data = []
with open('input.txt') as file:
    for i in file:
        data.append(int(i))

def find_sum(data: List[int], needle: int, start:int, end: int):
    seen = {}
    # print("Searching range:", start, end)
    for i in range(start, end):
        val = data[i]
        needed = needle - val
        # print("Checking for {}={}-{}".format(needed, needle, val))
        if needed in seen:
            return
        else:
            seen[val] = 1

    raise Exception("Missing value", needle)
def get_max_min_sum(data, start, end):
    max = min = data[start]
    for i in range(start, end):
        if data[i] < min:
            min = data[i]
        elif data[i] > max:
            max = data[i]
    
    return max + min
        

def find_contig_sum(needle, data):
    start, end = 0, 1
    seq = data[start] + data[end]

    while seq != needle and end < len(data):
        print("Loop one ({}, {}) = {}".format(start, end, seq))
        if seq > needle:
            print("Seq too great, decrease")
            seq -= data[start]
            start += 1
        elif seq < needle:
            end += 1
            seq += data[end]
    
    if seq == needle:
        print("Found: ({}, {}) = {}".format(start, end, get_max_min_sum(data, start, end)))

find_contig_sum(14360655, data)
# find_contig_sum(127, data)

# for i in range(window, len(data)):
#     val = data[i]

#     start, end = i - window, i
#     try:
#         find_sum(data, data[i], start, end)
#     except Exception as ex:
#         print("Success", ex)
#         exit