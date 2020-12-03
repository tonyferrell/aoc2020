
class InfinteWidthMap:

    def __init__(self, filename):
        self.tree_char = '#'
        self.open_char = '.'
        self._base_map = []
        self.height = 0

        with open(filename) as map:
            for row_raw in map:
                row = [m for m in row_raw]
                self.width = len(row)
                self._base_map.append(row)
            
            self.height = len(self._base_map)
    
    def get_position(self, x, y):
        a_x = x % self.width

        if y > self.height:
            raise Exception("Too far!")

        a_char = self._base_map[y][a_x] 
        print("Getting ({}, {} = {})".format(a_x+1, y+1, a_char))
        return a_char
    
    def is_tree(self, x, y):
        c = self.get_position(x,y)
        return c == self.tree_char

    def get_height(self):
        return self.height

def part1():
    m = InfinteWidthMap('input.txt')
    tree_count = 0
    x = 0
    for y in range(1, m.get_height()):
        x += 3
        if m.is_tree(x, y):
            tree_count += 1
    
    print("You hit {} trees".format(tree_count))

part1()