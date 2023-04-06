from collections import deque
import hashlib

class Move:
    def __init__(self, move_string, creator):
        self.hash = hashlib.sha256(move_string.encode()).hexdigest()
        self.creator = creator

    def __str__(self):
        return_string = f"{self.hash}: sent by {self.creator}"
        return return_string 

class Blockchain:
    def __init__(self):
        self.chain_length = 0
        self.difficulty = 3
        self.chain = deque()

class Block:
    def __init__(self) -> None:
        self.moves = {0 : Move,
                      1 : Move}
        self.move_number = 0
        self.root = ""
        self.previous_hash = ""
        self.previous_block_number = 0
        self.winning_miner = ""
        self.final_hash = ""
        self.blockchain = Blockchain()

    def add_move(self, move: Move):
        self.moves[self.move_number] = move
        if self.move_number == 1:
            self.find_root()
            self.proof_of_work()
        self.move_number += 1
            
    def find_root(self):
        temp_str = self.moves[0].__str__() + self.moves[1].__str__()
        self.root = hashlib.sha256(temp_str.encode()).hexdigest()
    
    def add_to_chain(self, blockchain: Blockchain):
        self.previous_block_number = blockchain.chain_length
        blockchain.chain.append(self)
        blockchain.chain_length += 1

    def proof_of_work(self):
        print(self.root)
        miner = input("Miner please enter your name: ")
        miner_address = hashlib.sha256(miner.encode()).hexdigest()
        nonce = input("Miner please enter the nonce you found: ")
        blockhash = miner_address + self.previous_hash + self.root + nonce
        hash = hashlib.sha256(blockhash.encode()).hexdigest()
        if hash[0:self.blockchain.difficulty] == "0" * self.blockchain.difficulty:
            self.final_hash = hash
            self.add_to_chain()
        else:
            self.proof_of_work()


# block1 = Block()
# block1.add_move(Move("Rock123", "Wyatt"))
# block1.add_move(Move("Scissors123", "WyattL"))
# print(block1.root)
