import os
from queue import Queue


class ChessBoard:
    cells = dict()
    knight_move_options = ((2, -1), (2, 1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2),
                           (-2, -1))

    def __init__(self, dimension: int):
        self.dimension = dimension

    def is_in_board(self, x_dimension: int, y_dimension: int) -> bool:
        if 0 < x_dimension <= self.dimension and 0 < y_dimension <= self.dimension:
            return True
        return False

    def visit_cell(self, src_cell, dest_cell):
        if dest_cell in self.cells or not self.is_in_board(*dest_cell):
            return None

        self.cells[dest_cell] = (self.cells[src_cell] + 1) if src_cell else 0
        return dest_cell

    @staticmethod
    def sum_cells(c1: tuple, c2: tuple) -> tuple:
        return c1[0] + c2[0], c1[1] + c2[1]

    def possible_knight_moves(self, cell: tuple) -> list:
        return list(
            filter(lambda i: i is not None, (self.visit_cell(src_cell=cell, dest_cell=self.sum_cells(m, cell)) for m in
                                             self.knight_move_options)))

    def get_level(self, cell):
        return self.cells[cell]


def game():
    # initiation
    default_dimension = os.getenv('DIMENSION')
    chess_board = ChessBoard(int(input(
        f'Default Dimension is {default_dimension}. Please Enter your own dimension or press enter: ') or default_dimension))
    source = tuple(map(int, input('Where is the Knight? (Enter coordinates space separated. Like 1 2.) --> ').split()))
    destination = tuple(
        map(int, input('Where is the Knight going? (Enter coordinates space separated. Like 10 6.) --> ').split()))

    chess_board.visit_cell(None, source)
    queue = Queue()
    queue.put(source)
    while queue.qsize():
        cell = queue.get()
        possible_moves = chess_board.possible_knight_moves(cell)
        for move in possible_moves:
            if move == destination:
                return f'Destination reached with {chess_board.get_level(move)} moves'
        else:
            for c in possible_moves:
                queue.put(c)
    return 'Not Possible!'


if __name__ == '__main__':
    print(game())
