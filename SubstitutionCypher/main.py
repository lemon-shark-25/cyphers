from substitutionCypher import SubstitutionCypher 

running = True
option = 0
text = ""
result = ""
cypher = SubstitutionCypher()

def menu():
    print("--- Substitution cypher ---")
    print("1. Get current key")    
    print("2. Generate key")
    print("3. Set key")
    print("4. Encrypt a message")
    print("5. Decrypt a message")
    print("6. Close programme")

while running:
    menu()
    option = int(input("Choose an option: "))

    match option:
        case 1:
            print(f"Current key: {cypher.getKey()}")
        case 2:
            result = cypher.genEncryptKey()
            print(f"Key: {result}")
            result = ""
        case 3:
            text = input("Input the new key (a string of all alphabet characters):\n")
            if cypher.isValidKey(text):  
                cypher.setKey(text)
                print("Key changed.")
            else:
                print("That is not a valid key.")
            text = ""
        case 4:
            text = input("Input the text you want to encrypt: \n") 
            result = cypher.subsEncrypt(text)
            print(f"Encrypted text: {result}")
            text = result = ""
        case 5:
            text = input("Input the text you want to decrypt: \n")
            result = cypher.subsDecrypt(text)
            print(f"Encrypted text: {result}")
            text = result = ""
        case 6:
            running = False
            print("Closing programme.")
        case _: 
            print("That is not a valid option.")
    input()
