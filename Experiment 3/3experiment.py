import hashlib
import random

challenge = random.randint(700,1400)
print("Challenge is: ",challenge)

Password = "yoyo"

Together = Password + str(challenge)

hash1 = hashlib.sha256(Together.encode()).hexdigest()
print("User Hash: ",hash1)


server = hashlib.sha256((Password + str(challenge)).encode()).hexdigest()
print("Server Hash",server)
if hash1 == server:
    print("Authentication Successfull")
else:
    print("Authentication fail")

