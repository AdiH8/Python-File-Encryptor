import secrets

def Encrypt(filename):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    key = secrets.token_bytes(16)
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key[index % len(key)]
        
    file = open("CC-" + filename, "wb")
    file.write(data)
    file.close()
    
    return key
    
def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key[index % len(key)]
        
    file = open(filename, "wb")
    file.write(data)
    file.close()
    

choice = ""
while choice != "3":
    print("Please select you option.")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Quit")
    choice = input()
    if choice == "1" or choice == "2":
        filename = input("Enter filename with extension:\n")
    if choice == "1":
        key = Encrypt(filename)
        print("Encryption key:", key.hex())
    if choice == "2":
        key_hex = input("Enter the decryption key (in hex):\n")
        key = bytes.fromhex(key_hex)
        Decrypt(filename, key)
