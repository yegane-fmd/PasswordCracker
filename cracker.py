import csv
import hashlib

# مرحله 1: خواندن فایل CSV و جدا کردن اسم و هش
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

# مرحله 2: حدس زدن عدد 4 رقمی برای هر هش
cracked_passwords = {}

for i in range(10000):
    password = f"{i:04d}"  # عدد رو به رشته ۴ رقمی تبدیل می‌کنیم (مثلاً 0001، 0234)
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    for idx, target_hash in enumerate(hashes):
        if password_hash == target_hash:
            cracked_passwords[names[idx]] = {
                "password": password,
                "hash": target_hash
            }

# مرحله 3: چاپ دیکشنری نهایی
print("\nCracked Passwords:")
for name, info in cracked_passwords.items():
    print(f"{name}: {info['password']} -> {info['hash']}")