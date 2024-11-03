from cryptography.fernet import Fernet

# Generate a new Fernet key
key = Fernet.generate_key()

# Save the key to a file
with open("key.key", "wb") as key_file:
    key_file.write(key)

print("Key generated and saved to key.key")
