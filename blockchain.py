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





# Part 2 - Mining our Blockchain

