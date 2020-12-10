lines = []
with open("input.txt") as data:
    for line in data:
        lines.append(int(line))

lines.append(0)
lines.sort()
lines.append(lines[-1]+3)

counts = [0] * len(lines)
counts[-1] = 1

for i in range(0, len(lines)):
    idx = len(lines) - i - 1
    curr_val = lines[idx]
    count = 0
    for s_i in range(idx, len(lines)):
        n = lines[s_i]

        if n-curr_val <= 3:
            count += counts[s_i]
        else:
            break
    
    counts[idx] = count

print(lines)
print(counts)