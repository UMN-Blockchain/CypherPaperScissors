from hashlib import sha256

miner_name = "Wyatt"
miner_address = sha256(miner_name.encode()).hexdigest()
block_hash = "d395fa355da2a6caa19e7c64afc58c82a9e16ef7cd11a517107d26371bd9c063"
to_hash = miner_address + block_hash
max_run = 10000 # Limits the amount of loops in case of errors
difficulty = 3

def hash(to_hash, max_run = 10000, difficulty = 3):
    for i in range(1, max_run):
        nonce = str(i)
        to_hash = to_hash + nonce
        hash = sha256(to_hash.encode()).hexdigest()
        if hash[0:difficulty] == "0" * difficulty:
            return nonce
    return "No Hash Found"

print(hash(to_hash, max_run, difficulty))