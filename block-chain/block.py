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
        self.nonce = 0
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        # print("transaction" + [t.to_dict() for t in self.transactions])
        block_string = json.dumps({
            "index" : self.index,
            "timestamp" : self.timestamp,
            "transactions" : [t.to_dict() for t in self.transactions],
            "previous_hash" : self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self, difficulty):
        target = "0" * difficulty
        
        while self.hash[:difficulty] != target:
            self.nonce +=1
            self.hash = self.calculate_hash()
            
        print("Yeees, Hi everyone horaaaa, you can check")
        print("Block mined:", self.hash)
        
        
        
class Blockchain:
    def __init__(self):
        self.difficulty = 4
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, [], "0")
    
    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        block = Block(
            len(self.chain),
            transactions,
            self.get_latest_block().hash
        )
        
        block.mine_block(self.difficulty)
        self.chain.append(block)
    

bc = Blockchain()

tx1 = Transaction("Reza", "Bobi", 10)
tx2 = Transaction("Bobi", "Charlie", 5)
bc.add_block([tx1, tx2])

tx3 = Transaction("Charlie", "Mahsa", 2)
bc.add_block([tx3])

for block in bc.chain:
    print("Block:", block.index)
    print("Hash:", block.hash)
    print("previous_hash:", block.previous_hash)
    print("Transactions:", [t.to_dict() for t in block.transactions])
    print("Nonce:", block.nonce)
    print()