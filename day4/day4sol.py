class Passport:
    req_fields = [
        'byr', # (Birth Year)
        'iyr', # (Issue Year)
        'eyr', # (Expiration Year)
        'hgt', # (Height)
        'hcl', # (Hair Color)
        'ecl', # (Eye Color)
        'pid', # (Passport ID)
        #'cid', # (Country ID)
    ]

    def __init__(self, start_line):
        self._start_line = start_line
        self._lines = []
        self._fields = {}
    
    def add_line(self, line: str):
        self._lines.append(line)
        try:
            for kvp in line.split(" "):
                if kvp:
                    self.add_field(kvp)
        except:
            print("Failed while processing the line: '{}'".format(line))
            raise
    
    def add_field(self, kvp):
        try:
            field, value = kvp.split(':')
            self._fields[field] = value
        except:
            print("Failed to extract from '{}'".format(kvp) )
            raise
    
    def validate(self) -> bool:
        for field in self.req_fields:
            if not field in self._fields:
                print("Missing field", field)
                return False

        return True
    
    def __str__(self) -> str:
        end_line = self._start_line + len(self._lines) - 1
        return "{}-{}: {}".format(self._start_line, end_line, ",".join(self._lines))

def part1():
    total = 0
    count = 0
    with open('input.txt') as data:
        line_num = 0
        next_passport: Passport = None
        for line in data:
            line_num += 1
            if next_passport is None:
                next_passport = Passport(line_num)
            line = line.strip()
            try:
                if line:
                    next_passport.add_line(line)
                else:
                    total += 1
                    if next_passport.validate():
                        count += 1
                        print("Valid Passport:", next_passport)
                    else:
                        print("Invalid Passport:", next_passport)

                    next_passport = None
            except:
                print("Failed on line {}: {}".format(line_num, line))
                raise
        
    print("Processed: {}, Valid: {}".format(total, count))

part1()