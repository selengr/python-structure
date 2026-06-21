import hashlib
import json
import time


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    
    def to_dict(self):
        return {
            "sender" : self.sender,
            "receiver" : self.receiver,
            "amount" : self.amount
        }

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        print("transaction" + [t.to_dict() for t in self.transactions])
        block_string = json.dumps({
            "index" : self.index,
            "timestamp" : self.timestamp,
            "transactions" : [t.to_dict() for t in self.transactions],
            "previous_hash" : self.previous_hash,
        }, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()
        

class Blockchain:
    
    
    