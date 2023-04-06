from move import Move

class Block:
    def __init__(self) -> None:
        self.moves = []
        self.move_count = 0
        self.root = ""

    def add_move(self, move: Move):
        self.moves.append(move)
        self.move_count = len(self.moves)

    def find_root(self):
        moves_copy = self.moves
        for i in range(1, len(moves_copy)):
            moves_copy[i]

block1 = Block()
block1.add_move()