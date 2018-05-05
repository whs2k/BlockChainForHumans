
import hashlib as hasher
import random
#import Image
import requests

'''
1. Create  Blocks

'''
class exclusiveRight:
	def __init__(self, index, timestamp, data, last_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.last_hash = last_hash
		self.hash = self.hash_right()

	def hash_right(self):
		sha = hasher.sha256()
		sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.last_hash)).encode("UTF-8"))
		return sha.hexdigest()

	def data(self):
		self.authors = authors
		self.claims = claims
		self.cpcs = cpcs
		self.localCPC = localCPC
		self.abstract = abstract
		self.detailedDescription = detailedDescription
		self.drawings = drawings  #images
		self.challengs = challenges #PTAB
		self.officeAction = officeAction
		self.langauge = langauge
		self.citations = citations #referneces
		self.country = country
		self.category = category #utility, plant, design, trademark, etc

	def hash_image(self):
		image = Image.open(self)
		return hasher.sha256(image.tostring()).hexdigest()

	def get_random_image(self):
		url = 'https://picsum.photos/200/300/?random'
		r = requests.get(url)
		image_data = r.content
		return image_data


'''
2. Create  First Block by Hand

'''

import datetime as date

def create_genesis_right():
	#Make the first by hand
	#index = 0; 
	#last_hash = rand
	return exclusiveRight(0, date.datetime.now(), "Gensis Contract", "0")

'''
3. Make Next Block

'''

def next_right(last_right):
  this_index = last_right.index + 1
  this_timestamp = date.datetime.now()
  this_data = "Hey! I'm patent " + str(this_index)
  this_hash = last_right.hash
  return exclusiveRight(this_index, this_timestamp, this_data, this_hash)

'''
4. Create a Chaning of 19 Contracts, and add Genesis

'''

 # Create the blockchain and add the genesis block
rightsChain = [create_genesis_right()]
last_right = rightsChain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_rights_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_rights_to_add):
  right_to_add = next_right(last_right)
  rightsChain.append(right_to_add)
  last_right = right_to_add
  # Tell everyone about it!
  print("Right #{} has been added to the rightsChain!".format(right_to_add.index))
  print("Hash: {}\n".format(right_to_add.hash))
