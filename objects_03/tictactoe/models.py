from enum import Enum
from typing import List, Tuple


class Cell(Enum):
    x = "X"
    o = "O"

    def __str__(self):
        return self.value


class Player:
    def __init__(self, name: str, cell_type: Cell):
        self.name = name
        self.cell_type = cell_type

    def __str__(self):
        return self.name


class Board:
    SIZE = 3

    board_str = "{} | {} | {}\n" \
                "---------\n" \
                "{} | {} | {}\n" \
                "---------\n" \
                "{} | {} | {}"

    def __init__(self):
        self.cells = [[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]]

    def __str__(self):
        return self.board_str.format(self.cells[0][0], self.cells[0][1], self.cells[0][2],
                                     self.cells[1][0], self.cells[1][1], self.cells[1][2],
                                     self.cells[2][0], self.cells[2][1], self.cells[2][2])

    def place(self, pos: int, cell_type: Cell):
        coord = self.int_to_coord(pos)
        self.cells[coord[0]][coord[1]] = cell_type

    def int_to_coord(self, integer: int) -> Tuple[int, int]:
        return divmod(integer, self.SIZE)

    def is_availabe(self, pos: int) -> bool:
        coord = self.int_to_coord(pos)
        try:
            return type(self.cells[coord[0]][coord[1]]) == int
        except IndexError:
            return False


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.board = Board()
        self.players = [player1, player2]
        self.turn = 0

    def play(self) -> Player or None:
        game_end = False
        while not game_end:
            print(self.board)
            placed = False
            while not placed:
                place = self.get_place()
                if self.board.is_availabe(place):
                    self.board.place(place, self.players[self.turn].cell_type)
                    placed = True
                else:
                    print("Spot not available")
            if self.has_won(self.players[self.turn]):
                return self.players[self.turn]
            if self.has_end():
                return None
            self.next_turn()

    def next_turn(self):
        self.turn += 1
        self.turn %= 2

    def get_place(self) -> int:
        output = False
        place = None
        inp = input("{player} ({sym}), your turn, pick an empty spot to place your mark\n".format(
            player=self.players[self.turn],
            sym=self.players[self.turn].cell_type))
        while not output:
            try:
                place = int(inp)
                output = True
            except ValueError:
                inp = input("Input must be of type integer")
        return place

    # board checks
    def has_diagonal(self, player: Player) -> bool:
        line = True
        for i in range(0, self.board.SIZE):
            if not self.board.cells[i][i] == player.cell_type:
                line = False
                break
        if line:
            return line
        line = True
        for i in range(0, self.board.SIZE):
            if self.board.cells[i][self.board.SIZE - i - 1] != player.cell_type:
                line = False
                break
        return line

    def has_row(self, player: Player) -> bool:
        for row in self.board.cells:
            line = True
            for cell in row:
                if cell != player.cell_type:
                    line = False
                    break
            if line:
                return line
        return False

    def has_column(self, player: Player) -> bool:
        for col in range(0, self.board.SIZE):
            line = True
            for cell in range(0, self.board.SIZE):
                if self.board.cells[cell][col] != player.cell_type:
                    line = False
                    break
            if line:
                return line
        return False

    def has_won(self, player: Player) -> bool:
        return self.has_column(player) or self.has_diagonal(player) or self.has_row(player)

    def has_end(self):
        for row in self.board.cells:
            for cell in row:
                if type(cell) == int:
                    return False
        return True
