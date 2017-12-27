
import hashlib as hasher
import random

'''
1. Create  Blocks

'''
class smartContract:
	def __init__(self, index, timestamp, data, last_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.last_hash = last_hash
		self.hash = self.hash_contract()

	def hash_contract(self):
		sha = hasher.sha256()
		sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.last_hash)).encode("UTF-8"))
		return sha.hexdigest()
'''
2. Create  First Block by Hand

'''

import datetime as date

def create_genesis_contract():
	#Make the first by hand
	#index = 0; 
	#last_hash = rand
	return smartContract(0, date.datetime.now(), "Gensis Contract", "0")

'''
3. Make Next Block

'''

def next_contract(last_contract):
  this_index = last_contract.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Hey! I'm contract " + str(this_index)
  this_hash = last_contract.hash
  return smartContract(this_index, this_timestamp, this_data, this_hash)

'''
4. Create a Chaning of 19 Contracts, and add Genesis

'''

 # Create the blockchain and add the genesis block
contractChain = [create_genesis_contract()]
last_contract = contractChain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_contracts_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_contracts_to_add):
  contract_to_add = next_contract(last_contract)
  contractChain.append(contract_to_add)
  last_contract = contract_to_add
  # Tell everyone about it!
  print("Contract #{} has been added to the Dealchain!".format(contract_to_add.index))
  print("Hash: {}\n".format(contract_to_add.hash))
