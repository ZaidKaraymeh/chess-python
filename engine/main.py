from dataclasses import dataclass, asdict, field
from pprint import pprint as p
from tracemalloc import start

from fen import FenParser

@dataclass
class Piece:
    """
        Class for pieces
    """

    piece: str
    color: str


@dataclass
class Board:
    """
        Class for managing all pieces
    """
    turn: bool = field(init=False)
    state : list[str] = field(init=False)
    state_pieces: list[Piece] = field(init=False)
    start_pos = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

        
    def __post_init__(self):
            parser = FenParser(self.start_pos)
            self.state = parser.parse()
            self.turn = False
            self.draw_board(self.start_pos)

    def draw_board(self, pos):
        docs = {
            "k":Piece("King", 'Black'),
            "K":Piece("King", 'White'),
            "q":Piece("Queen", 'Black'),
            "Q":Piece("Queen", 'White'),
            "r":Piece("Rook", 'Black'),
            "R":Piece("Rook", 'White'),
            "b":Piece("Bishop", 'Black'),
            "B":Piece("Bishop", 'White'),
            "n":Piece("Knight", 'Black'),
            "N":Piece("Knight", 'White'),
            "p":Piece("Pawn", 'Black'),
            "P":Piece("Pawn", 'White'),
        }
        # pieces = [
        #     [
        #         Piece("Knight", "Black") for x in range(8)
        #     ] for x in range(8)
        # ]

        # def parser(self, char):
        #     if char.isnumeric():
        #         return ["-" for x in range(int(char))]
            
        #     return docs[char]


        pos_split, *rest = pos.split(" ")
        pos_split = pos_split.replace("/", "")

        def parse(row):
            for char in row:
                if char.isnumeric():
                    yield from ['-']*int(char)
                else:
                    yield docs[char]
        def parse_board(FEN):
            return [list(map(parse,k)) for k in FEN.split('/')]

        parsed_fen = parse_board(pos_split)
        print(parsed_fen)
        pieces = list(
            map(
                lambda x: parse(self, x),
                pos_split
            )
        )
        # pieces = list(filter(lambda x: type(x) == Piece, pieces))
        self.state_pieces = pieces

    def board_state(self, state):
        parser = FenParser(state)

board = Board()
p(board.state_pieces)

