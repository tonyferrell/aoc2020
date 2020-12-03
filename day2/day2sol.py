with open('input.txt') as data:
    valid = 0
    for line in data:
        char_range, char, password = line.split(' ')
        min, max = char_range.split('-')
        min, max = int(min), int(max)
        char = char[0]

        count = 0
        for c in password:
           if c == char:
               count += 1
            
        if min <= count and count <= max:
            print(password, "is valid")
            valid += 1
    print("There are {} valid passwords".format(valid))