with open('input.txt') as data:
    departure = int(next(data))
    r = next(data)
    times = [int(x) if x != 'x' else 0 for x in r.split(",")]


num = d_n = times[0]
# num = 100000000000000
# num = 102563359500841
# d_n = max(times)
adj = times.index(d_n)

while num == 0 or num % d_n != 0:
    num += 1

print("Starting at {}, delta of {}".format(num, d_n))

times = list(filter(lambda x: x[1] > 0, list(enumerate(times))))
print(times)

c = 0
while True:
    c += 1
    if c % 500000 == 0:
        print("Checking", num)
    success = True

    match = 1
    for i, v in times:
        if v == 0:
            continue

        c = (num - adj + i)


        # print("Trying {}: ({}) {} != 0".format(num, v, c % v))
        if c % v != 0:
            success = False
            break
        
        match *= v
        if match > d_n:
            d_n = match
            print("New delta", d_n)

    if success:
        print("{} was the number!".format(num - adj))
        break
    
    num += d_n