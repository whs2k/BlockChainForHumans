import hashlib as hasher
import random

print(hasher.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest())


def hash_contract(self):
		sha = hasher.sha256()
		sha.update(str(self.index) +
                                str(self.timestamp) + 
				str(self.last_hash) +
                                str(self.data) +
                                str(self.last_hash))
		return (str(random.getrandbits(256)).encode('utf-8')).hexdigest()
import hashlib

message = 'whatever'.encode()

code = hashlib.sha256(message).hexdigest()

print(code)
