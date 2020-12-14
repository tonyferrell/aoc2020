from typing import List
from functools import reduce


def print_board(g_board):
    for line in g_board:
        print("".join(line))


class LifeBoard:
    search_dirs = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],

        [-1, -1],
        [1, 1],
        [1, -1],
        [-1, 1]
    ]

    def __init__(self, board: List[List[str]], hash: List[int]):
        self.board = board
        self.row_count = len(board)
        self.col_count = len(board[0])
        self.hash_list = hash

    @classmethod
    def build_input_board(cls, file: str) -> 'LifeBoard':
        with open(file) as data:
            board = []
            hash_list = []
            col_count = None
            for line in data:
                line = line.strip()
                row = list(line)
                n_col = len(row)
                if col_count is None:
                    col_count = n_col
                elif col_count != n_col:
                    raise Exception(
                        "Non-matching column count: {}!={}".format(col_count, n_col))

                board.append(row)

                row_hash = 0
                for i in row:
                    bit = 1 if i == '#"' else 0
                    row_hash = (row_hash << 1) | bit

                hash_list.append(row_hash)

            return LifeBoard(board, hash_list)

    def __str__(self):
        str = ""
        for i in range(0, self.row_count):
            str += "{:05d} : {}\n".format(
                self.hash_list[i], "".join(self.board[i]))

        return str

    def __eq__(self, o: object) -> bool:
        if isinstance(o, LifeBoard):
            if len(self.hash_list) != len(o.hash_list):
                return False

            return reduce(lambda cum, elem: cum and elem[0] == elem[1], zip(self.hash_list, o.hash_list))

        return False

    def get_adj_count(self, row: int, col: int, verbose=False) -> int:
        adj = 0
        for d_r, d_c in self.search_dirs:
            n_r = row
            n_c = col
            if verbose:
                print("Looking for adjacents for ({}, {}) with delta ({}, {})".format(row, col, d_r, d_c))
            while True:
                n_r = n_r + d_r
                n_c = n_c + d_c

                if n_r < 0 or n_r >= self.row_count or n_c < 0 or n_c >= self.col_count:
                    # No chairs this direction - we reached the end of the board
                    break

                next = self.board[n_r][n_c] 
                if verbose:
                    print("Checking ({}, {}) = {}".format(n_r, n_c, next))
                if next == '.':
                    if verbose:
                        print("Floor - skipping")
                    # This isn't a chair - keep looking
                    continue

                if next == '#':
                    if verbose:
                        print("Occupied Chair")
                    adj += 1

                break

        if verbose:
            print("### Total Adjacents: ({}, {}) = {}".format(row,col, adj))
        return adj

    def next_seating(self):
        adj_board = []
        hashes = []
        for r in range(0, self.row_count):
            new_row = []
            row_hash = 0
            for c in range(0, self.col_count):
                curr = self.board[r][c]
                new_seat = curr
                
                verbose = False
                adj = self.get_adj_count(r,c, verbose)
                if curr == 'L' and adj == 0:
                    new_seat = '#'
                elif curr == '#' and adj >= 5:
                    new_seat = 'L'

                row_hash = (row_hash << 1) | (1 if new_seat == '#' else 0)
                new_row.append(new_seat)

            adj_board.append(new_row)
            hashes.append(row_hash)

        return LifeBoard(adj_board, hashes)
    
    def full_seats(self) -> int:
        return sum([sum([1 if digit=='1' else 0 for digit in bin(n)[2:]]) for n in self.hash_list])



def part1():
    prev = LifeBoard.build_input_board('input.txt')

    for i in range(1000):
        print("Board {}".format(i))
        # print(prev)
        next = prev.next_seating()
        if next == prev:
            print("Found Stable Board on iter {} with {} seats".format(i, next.full_seats()))
            print(next)
            break

        prev = next


part1()
