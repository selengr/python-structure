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
    def __init__(self):
        self.chain = []
        
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, transactions):
        new_block = Block(
            index=len(self.chain),
            transactions=transactions,
            previous_hash=self.get_latest_block().hash
        )
        self.chain.append(new_block)
    

bc = Blockchain()

tx1 = Transaction("Reza", "Bobi", 10)
tx2 = Transaction("Bobi", "Charlie", 5)

bc.add_block([tx1,tx2])

tx3 = Transaction("Charlie", "Mahsa", 2)
bc.add_block([tx3])

for block in bc.chain:
    print("Block:", block.index)
    print("Hash:", block.hash)
    print("Prev:", block.previous_hash)
    print("Transactions:", [t.to_dict() for t in block.transactions])
    print()