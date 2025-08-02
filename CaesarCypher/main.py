from caesarCypher import caesarEncrypt, caesarDecrypt, caesarForceDecrypt

running = True
key = 0
text, result = "", ""

def menu():
    print("--- Caesar Cypher ---")
    print("1. Set a key.")
    print("2. Encrypt a message.")
    print("3. Decrypt a message.")
    print("4. Force decrypt a message.")
    print("5. Exit.")

while running:
    menu()
    
    option = int(input("Choose an option: "))
    
    match option:
        case 1:
            key = int(input("Input the key (must be a number): "))
        case 2:
            text = input("Write the text you want to encrypt: ")      
            result = caesarEncrypt(text, key)
            print(f"Encrypted message: {result}")
        case 3:
            text = input("Write the text you want to decrypt: ")
            result = caesarDecrypt(text, key)
            print(f"Decryption: {result}")
        case 4:
            text = input("Write the text you want to force decrypt: ")
            caesarForceDecrypt(text)
        case 5:
            running = False
            print("Closing programme.")
        case _:
            print("That's not an option.")
