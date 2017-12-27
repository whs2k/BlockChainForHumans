import hashlib as hasher

print(hasher.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest())
