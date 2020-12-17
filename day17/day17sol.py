from typing import Deque


class Cube:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

class Board:
    def __init__(self):
        self.max_x = None
        self.min_x = None

        self.max_y = None
        self.min_y = None

        self.max_z = None
        self.min_z = None

        self.max_w = None
        self.min_w = None

        self.state = {}
    
    def activate_cube(self, x, y, z, w):
        """
        Activate a cube!
        """
        self.maybe_update_bounds(x, y, z, w)
        c = Cube(x, y, z, w)
        self.state[(x,y,z,w)] = c

    def maybe_update_bounds(self, x, y, z, w):
        if self.max_x is None:
            self.max_x = x
        elif self.max_x < x:
            self.max_x = x

        if self.min_x is None:
            self.min_x = x
        elif self.min_x > x:
            self.min_x = x
        
        if self.max_y is None:
            self.max_y = y
        elif y > self.max_y:
            self.max_y = y
        
        if self.min_y is None:
            self.min_y = y
        elif y < self.min_y:
            self.min_y = y
        
        if self.max_z is None:
            self.max_z = z
        elif self.max_z < z:
            self.max_z = z

        if self.min_w is None:
            self.min_w = w
        elif z < self.min_w:
            self.min_w = w


    
    def check_cube(self, x, y, z, w):
        key = (x,y,z,w)
        if not key in self.state:
            return
    
    def get_active_neighbor_count(self,x,y,z, w, cap = -1):
        neighbors = self.get_neighbors(x, y, z, w)

        count = 0
        for n in neighbors:
            if n in self.state:
                count += 1 
            
            if cap > 0 and count > cap:
                return count
        
        return count

    def get_neighbors(x, y, z, w):
        for d_x in [-1, 0, 1]:
            for d_y in [-1, 0, 1]:
                for d_z in [-1, 0, 1]:
                    for d_w in [-1, 0, 1]:
                        if d_x == d_y and d_y == d_z and d_z == d_w and d_z == 0:
                            continue

                        yield (x + d_x, y + d_y, z + d_z, w + d_w)
    
    def is_active(self, x, y, z, w):
        return (x,y,z,w) in self.state

    def print_layer(self, z_filt):
        for x,y,z in self.state:
            if z == z_filt:
                print("({}, {})".format(x,y))

    def iter_board(self) -> 'Board':
        """
        Look at ever cube's current state, track its neighbors, be sure not to 
        double check cubes
        """
        verbose = False
        new_board = Board()
        visited_cubes = set()
        dq = Deque()
        for loc, _ in self.state.items():
            x, y, z, w = loc

            visited_cubes.add(loc)
            active_neighbor_count = 0

            for n in Board.get_neighbors(x,y,z,w):
                dq.append(n)
                n_x, n_y, n_z, n_w = n

                if self.is_active(n_x, n_y, n_z, n_w):
                    active_neighbor_count += 1

            if active_neighbor_count == 2 or active_neighbor_count == 3:
                new_board.activate_cube(x, y, z, w)
                if(verbose):
                    print("Activating neighbor! {}".format(loc))
        
        for loc in dq:
            if loc in visited_cubes:
                continue

            x, y, z, w = loc
            visited_cubes.add(loc)

            count = 0
            for n in Board.get_neighbors(x,y,z, w):
                if count > 3:
                    break

                n_x, n_y, n_z, n_w = n
                if self.is_active(n_x, n_y, n_z, n_w):
                    count += 1
            
            if count == 3:
                new_board.activate_cube(x, y, z, w)
        
        return new_board

    def get_active_cube_count(self):
        return len(self.state)
            
board = Board()
# Build the board
with open('input.txt') as data:
    z=w=0
    for y, line in enumerate(data):
        for x, rep in enumerate(line):
            if rep == '#':
                board.activate_cube(x,y,z,w)

print("Starting: ", board.get_active_cube_count())
# print(board.get_layer)
for i in range(6):
    board = board.iter_board()
    print("Iteration {} has {} active.".format(i, board.get_active_cube_count()))



