import hashlib

miner_name = "Wyatt"
miner_address = hashlib.sha256(miner_name.encode()).hexdigest()
block_hash = "e0841ec3e5e94f0cf3418faaa2c6c98bba10a35d06c134788e711be0bfa60d42"
to_hash = miner_address + block_hash
max_run = 10000 # Limits the amount of loops in case of errors
difficulty = 3

def hash(to_hash, max_run = 10000, difficulty = 3):
    for i in range(1, max_run):
        nonce = str(i)
        added_nonce = to_hash + nonce
        hash = hashlib.sha256(added_nonce.encode()).hexdigest()
        if hash[0:difficulty] == "0" * difficulty:
            print(f"{hash} found at nonce {nonce}\n")
            return nonce
    return "No Hash Found"

hash(to_hash, max_run, difficulty)