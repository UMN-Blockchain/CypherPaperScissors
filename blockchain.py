from block import Block, Move

class Blockchain:
    def __init__(self):
        self.chain_length = 0
        self.difficulty = 3
        self.chain = []
        self.last_hash = "N/A"

    def __str__(self) -> str:
        for node in self.chain:
            print(node)
        return "Done"
    
    def add_block(self):
        block = Block(self.difficulty, len(self.chain), previous_hash=self.last_hash)
        name = input("What is your name? ")
        play = input("What is your play? ")
        password = input("Enter a secret password: ")
        block.add_move(Move(play + password, name))
        name = input("What is your name? ")
        play = input("What is your play? ")
        password = input("Enter a secret password: ")
        block.add_move(Move(play + password, name))
        self.chain.append(block)
        self.last_hash = block.final_hash