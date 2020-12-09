from typing import List
window = 25

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

for i in range(window, len(data)):
    val = data[i]

    start, end = i - window, i
    try:
        find_sum(data, data[i], start, end)
    except Exception as ex:
        print("Success", ex)
        exit