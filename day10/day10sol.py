lines = []
with open("input.txt") as data:
    for line in data:
        lines.append(int(line))

# Add starting value
lines.append(0)
lines.sort()
# Add "power adapter" value
lines.append(lines[-1]+3)

# Memorize how many ways there are to reach the end from each value
counts = [0] * len(lines)
counts[-1] = 1

for i in range(0, len(lines)):
    # Start at the last value and work forward
    idx = len(lines) - i - 1
    curr_val = lines[idx]

    # Search forward until you find a value that is no longer within 3 jolts, 
    # and count how many ways those could reach the end.
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