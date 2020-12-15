with open('input.txt') as data:
    departure = int(next(data))
    r = next(data)
    times = [int(x) for x in r.split(",") if x != 'x']

print(times)

min_t = max(times)
min_mod = min_t
for t in times:
    mod = t - (departure % t)
    if mod < min_mod:
        min_t = t
        min_mod = mod

print(min_t *(min_t - (departure % min_t)))
