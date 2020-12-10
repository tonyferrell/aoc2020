lines = []
with open("input.txt") as data:
    for line in data:
        lines.append(int(line))

lines.sort()
lines.append(lines[-1]+3)
last = 0
diffs = [0,0,0]
for i in lines:
    diff = i - last
    print("New Diff:", diff)
    diffs[diff - 1] += 1
    last = i

print("All Diffs: {}. Mult:{}".format(diffs, diffs[0] * diffs[2]))