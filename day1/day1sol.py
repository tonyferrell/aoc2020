from functools import reduce

def part1():
    with open('input.txt') as data:
        seen = {}
        for line in data:
            num = int(line)

            needed = 2020 - num
            if needed in seen:
                print("Answer:", needed * num)
                break
            else:
                seen[num] = 1

def part2():
    input = []
    seen = {}
    with open('input.txt') as data:
        for x in data:
            val = int(x)
            seen[val] = [val]
            input.append(val)
    
    input.sort()

    size = len(input)

    # left = 0
    # right = size - 1
    # while True:
    #     low_val = input[left]
    #     high_val = input[right]

    #     if low_val + high_val > 2020 and left < right:
    #         right -= 1
    #         continue
        
    #     while low_val + high_val < 2020 and left < right:
    #         needed = 2020 - (low_val + high_val)
    #         if needed in seen:
    #             print("You did it ({}, {}, {}) = {}".format(low_val, needed, high_val, low_val * needed * high_val))
    #             exit()
    #         else:
    #             left += 1
    #             low_val = input[left]


    pairs = {}
    for i in range(0, size):
        for j in range(i+1, size):
            val1 = input[i]
            val2 = input[j]

            sum = val1 + val2
            if sum < 2020:
                if sum in pairs:
                    print("What happened?!")
                    continue

                pairs[val1+val2] = [val1, val2]
            else:
                # No more values in sorted list
                break

    for sum, items in pairs.items():
        needed = 2020 - sum
        if needed in seen:
            items.append(needed)
            calc = reduce(lambda x,y: x * y, items)
            print("You found it! ({}) = {}".format(items, calc))

part2()

