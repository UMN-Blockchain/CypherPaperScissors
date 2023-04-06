from move import Move
import hashlib

class Block:
    def __init__(self) -> None:
        self.moves = {0 : Move,
                      1 : Move}
        self.move_number = 0
        self.root = ""

    def add_move(self, move: Move):
        self.moves[self.move_number] = move
        if self.move_number == 1:
            self.find_root()
        self.move_number += 1
            

    def find_root(self):
        temp_str = self.moves[0].__str__() + self.moves[1].__str__()
        self.root = hashlib.sha256(temp_str.encode()).hexdigest()


block1 = Block()
block1.add_move(Move("Rock123", "Wyatt"))
block1.add_move(Move("Scissors123", "WyattL"))
print(block1.root)