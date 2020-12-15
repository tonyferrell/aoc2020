input = [12,1,16,3,11,0]
#input = [0,3,6]

seen = {}
said = input[0]
for i in range(0,30000000):
    last_said = said
    if i < len(input):
        said = input[i]
    elif said in seen:
        # print("Seen on {}. Saying {}".format(seen[said], i - seen[said]))
        said = i - seen[said]
    else:
        said = 0
        
    seen[last_said] = i
    print("{}: {}".format(i+1, said))
