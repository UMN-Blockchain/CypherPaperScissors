from blockchain import Blockchain

CypherPaperScissorsChain = Blockchain()


def play_CypherPaperScissors(block: Blockchain):
    CypherPaperScissorsChain.add_block()
    print(CypherPaperScissorsChain)
    
while True:
    play_CypherPaperScissors(Blockchain)
    cont = input("Input Y to continue N to stop")
    if cont == "N":
        break
