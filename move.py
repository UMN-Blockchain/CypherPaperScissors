import hashlib

class Move:
    def __init__(self, move_string, creator):
        self.hash = hashlib.sha256(move_string.encode()).hexdigest()
        self.creator = creator
    
    def __str__(self):
        return f"{self.hash}: sent by {self.creator}"
    
move = Move("WyattLindquist1234", "Wyatt Lindquist")
print(move)
