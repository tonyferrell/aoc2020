import re

def val_range(min: int, max: int):
    def g(x: str):
        if len(x) != 4:
            return False

        i_x = int(x)
        return min <= i_x and i_x <= max
    
    return g

in_match = re.compile("(\d+)in")
cm_match = re.compile("(\d+)cm")
def val_height(hgt: str) -> bool:
    i = in_match.match(hgt)
    if i:
        try:
            i_i = int(i.group(1))
            return 59 <= i_i and i_i <= 76 
        except:
            print("Bad Regex Data")
            return False
        
    c = cm_match.match(hgt)
    if c:
        try:
            i_c = int(c.group(1))
            return 150 <= i_c and i_c <= 193 
        except:
            print("Bad Regex Data")
            return False
    
    return False
   

hcl_valid = re.compile("^#[a-fA-F0-9]{6}$")
ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
passport = re.compile("^[0-9]{9}$")
class Passport:
    req_fields = {
        'byr': val_range(1920, 2002), # (Birth Year)
        'iyr': val_range(2010, 2020), # (Issue Year)
        'eyr': val_range(2020, 2030), # (Expiration Year)
        'hgt': val_height, # (Height)
        'hcl': lambda x: hcl_valid.match(x) is not None, # (Hair Color)
        'ecl': lambda x: x in ecl, # (Eye Color)
        'pid': lambda x: passport.match(x) is not None, # (Passport ID)
        #'cid', # (Country ID)
    }

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
        for field, pred in self.req_fields.items():
            if not field in self._fields:
                print("Missing field", field)
                return False
            elif not pred(self._fields[field]):
                return False

        return True
    
    def __str__(self) -> str:
        end_line = self._start_line + len(self._lines) - 1
        return "{}-{}: {}".format(self._start_line, end_line, ",".join(self._lines))

def part():
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

part()