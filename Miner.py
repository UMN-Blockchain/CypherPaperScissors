from hashlib import sha256
import random

miner_address = "[Insert Your Address]"
random.seed(miner_address)
block_hash = "[Hash of current block]"
to_hash = miner_address + block_hash
max_run = 10000 # Limits the amount of loops in case of errors
difficulty = 3

def hash(to_hash, max_run = 10000, difficulty = 3):
    for i in range(1, max_run):
        nonce = i
        to_hash = to_hash + nonce
        hash = sha256(to_hash.encode()).hexdigest()
        if hash[0:difficulty] == dif_string(difficulty):
            return hash
    return "No Hash Found"

def dif_string(difficulty):
    return_str = ""
    for i in range(0, difficulty):
        return_str = return_str + "0"
    return return_str

print(hash(to_hash, max_run, difficulty))