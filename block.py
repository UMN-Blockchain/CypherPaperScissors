import hashlib

class Move:
    def __init__(self, move_string, creator):
        self.hash = hashlib.sha256(move_string.encode()).hexdigest()
        self.creator = creator

    def __str__(self) -> str:
        return f"{self.hash}: sent by {self.creator}"

class Block:
    def __init__(self, difficulty, block_number, previous_hash = "N/A") -> None:
        self.block_number = block_number
        self.block_difficulty = difficulty
        self.moves = {0 : Move,
                      1 : Move}
        self.move_number = 0
        self.root = ""
        self.previous_hash = previous_hash
        self.winning_miner = ""
        self.final_hash = ""

    def __str__(self) -> str:
        return f"Block #: {self.block_number}\nBlock difficulty: {self.block_difficulty}\nPrevious Hash: {self.previous_hash}\nRoot Hash: {self.root}\nFinal Hash: {self.final_hash}\nWinning Miner: {self.winning_miner}\nMoves: {self.moves}\n\n"

    def add_move(self, move: Move):
        self.moves[self.move_number] = move
        if self.move_number == 1:
            self.find_root()
            self.proof_of_work()
        self.move_number += 1
            
    def find_root(self):
        temp_str = self.moves[0].__str__() + self.moves[1].__str__()
        self.root = hashlib.sha256(temp_str.encode()).hexdigest()
    
    def proof_of_work(self):
        blockhash = self.previous_hash + self.root
        blockhash = hashlib.sha256(blockhash.encode()).hexdigest()
        print(blockhash)
        miner = input("Miner please enter your name: ")
        miner_address = hashlib.sha256(miner.encode()).hexdigest()
        nonce = input("Miner please enter the nonce you found: ")
        blockhash = miner_address + blockhash + nonce
        hash = hashlib.sha256(blockhash.encode()).hexdigest()
        if hash[0:self.block_difficulty] == "0" * self.block_difficulty:
            self.final_hash = hash
            self.winning_miner = miner_address
        else:
            print(f"Not quite: we got {hash}")
            self.proof_of_work()


# block1 = Block()
# block1.add_move(Move("Rock123", "Wyatt"))
# block1.add_move(Move("Scissors123", "WyattL"))
# print(block1.root)
