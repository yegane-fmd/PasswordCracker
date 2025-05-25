import csv
import hashlib


names = []
hashes = []

with open('hashes_only.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        name, hash_value = row
        names.append(name)
        hashes.append(hash_value)
        print(f"Name: {name}, Hash: {hash_value}")


cracked_passwords = {}

for i in range(10000):
    password = f"{i:04d}"  
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    for idx, target_hash in enumerate(hashes):
        if password_hash == target_hash:
            cracked_passwords[names[idx]] = {
                "password": password,
                "hash": target_hash
            }


print("\nCracked Passwords:")
for name, info in cracked_passwords.items():
    print(f"{name}: {info['password']} -> {info['hash']}")
