from block import Block, Move, Blockchain

block = Block()


def play_CypherPaperScissors(block: Block):
    name = input("What is your name? ")
    play = input("What is your play? ")
    password = input("Enter a secret password: ")
    block.add_move(Move(play + password, name))
    
while True:
    play_CypherPaperScissors(block)
