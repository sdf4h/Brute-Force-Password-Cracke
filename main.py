import hashlib
import itertools

def brute_force_crack(hash_to_crack, charset, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt = ''.join(attempt)
            hashed_attempt = hashlib.md5(attempt.encode()).hexdigest()
            if hashed_attempt == hash_to_crack:
                return attempt
    return None

hash_to_crack = '5f4dcc3b5aa765d61d8327deb882cf99'  # Hash for "password"
charset = 'abcdefghijklmnopqrstuvwxyz'
max_length = 5

password = brute_force_crack(hash_to_crack, charset, max_length)
if password:
    print(f"Password found: {password}")
else:
    print("Password not found")
