import hashlib
import json
import time
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
print("---------app", app)
peers = set()
print("---------peers", peers)

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
        
        self.broadcast_block(block)
        
    def broadcast_block(self, block):
        for peer in peers:
            try:
                requests.post(f"http://{peer}/receive_block", json={
                    "index": block.index,
                    "transactions": [t.to_dict() for t in block.transactions],
                    "previous_hash": block.previous_hash,
                    "nonce": block.nonce,
                    "hash": block.hash,
                    "timestamp": block.timestamp
                })
            except:
                pass
    

bc = Blockchain()


@app.route('/add_peer', methods=['POST'])
def add_peer():
    data = request.get_json()
    peer = data.get("peer")
    peers.add(peer)
    return {"message": "peer added", "peers": list(peers)}

@app.route('/receive_block', methods=['POST'])
def receive_block():
    data = request.get_json()
    
    transactions = [
        Transaction(t["sender"], t["receiver"], t["amount"])
        for t in data["transactions"]
    ]
    
    block = Block(
        data["index"],
        transactions,
        data["previous_hash"]
    )
    
    block.nonce = data["nonce"]
    block.hash = data["hash"]
    
    bc.chain.append(block)
    
    return {"message": "block received"}

