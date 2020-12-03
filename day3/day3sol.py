from functools import reduce
class InfinteWidthMap:

    def __init__(self, filename):
        self.tree_char = '#'
        self.open_char = '.'
        self._base_map = []
        self.height = 0

        with open(filename) as map:
            for row_raw in map:
                if not row_raw:
                    print("Skipping", row_raw)
                    continue
                row = [m for m in row_raw]
                self.width = len(row)
                self._base_map.append(row)
            
            self.height = len(self._base_map)
    
    def get_position(self, x, y):
        a_x = x % self.width

        if y > self.height:
            raise Exception("Too far!")

        a_char = self._base_map[y][a_x] 
        # print("Getting ({}, {} = {})".format(a_x+1, y+1, a_char))
        return a_char
    
    def is_tree(self, x, y):
        c = self.get_position(x,y)
        return c == self.tree_char

    def get_height(self):
        return self.height

def part1():
    m = InfinteWidthMap('input.txt')
    traverses = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    a_t = []
    for d_x, d_y in traverses:
        tree_count = 0
        x = 0
        rows = range(0, m.get_height(), d_y)[1:]
        print("doing rows",rows)
        for y in rows:
            x += d_x
            if m.is_tree(x, y):
                tree_count += 1

        a_t.append(tree_count)
        print("You ({}, {}) hit {} trees".format(d_x, d_y, tree_count))

        total = reduce(lambda x,y: x*y, a_t)

    print("The total of {} is: {}".format(a_t, total))

part1()