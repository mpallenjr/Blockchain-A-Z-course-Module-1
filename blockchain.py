# Module 1 - Create a Blockchain

# Importing the libraries
import datetime # each block will have its own time stamp
import hashlib  # will be used to hash the blocks
import json # will use the dumps function from this library to encode them before hashing
from flask import Flask, jsonify #creats an object and json response to display the response

# Part 1 - Building a Blockchain

class Blockchain:  #Class will include Genesis Block, Initalize a Chain(init function),Create block function to add a new block and mine in the future, tools to keep it from being hacked
    
    def __init__(self): #init is always first statement and self is the param, when initalized will create an instance class of itself.
        self.chain = [] #creating an empty list/array function for the blockchain
        self.create_block(proof = 1, previous_hash = '0') #must put the 0 in quotes because the SHA256 encryption only accepts strings. Create block function

    def create_block(self, proof, previous_hash):
        block = {                                           #The block can also have a data key for this particular exercise there is no additional data. What will be represented in postman
            'index': len(self.chain) + 1,                   #The index will return the length of the blockchain
            'timestamp': str(datetime.datetime.now()),      #The timestamp will atuomatically apply date and time to the block when it is created. Must be in a string format. 
            'proof': proof,                                 #A function to be called on later. "The proof found or solved."
            'previous_hash': previous_hash                  #Links the previous block to this block
            }                 
        delf.chain.append(block)                            #appends the block, elongating 
        return block                                        #returns the created block as a value

    def get_previous_block(self):                           #function that returns the last block of the chain
        return self.chain[-1]

    def proof_of_work(self, previous_proof):                #The part of the data the the miner needs to find to claim this block.  The puzzle that needs to be challeneged by the miner.  Hard to find, but easy to verify.
        new_proof = 1                                       #To solve the problem you will increase New_proof by one at each increment of the while loop. 
        check_proof = False                                 #Used to stop the while loop once the check_proof becomes true
        while check_proof is False:                         
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest() #Must have a non symetrical operation here to avoid having the same proof in the operation. 
            if hash_operation[:4] == '0000':                #The more leading zeros, the harder it will be for the miner to crack the code. 
                check_proof = True
            else:
                new_proof += 1
        return new_proof
# Part 2 - Mining our Blockchain

