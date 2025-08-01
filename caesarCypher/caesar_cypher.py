def caesarEncrypt(message, key=0):
    # Initialize encrypted string
    encrypted = ""

    for i in range(len(message)):
        char = message[i]

        if (65 <= ord(char) <= 90):     # Check for uppercase 
            encrypted += chr(65 + (ord(char) - 65 + key) % 26)
        elif (97 <= ord(char) <= 122):  # Check for lowercase
            encrypted += chr(97 + (ord(char) - 97 + key) % 26)
        else:                           # Every other symbol
            encrypted += char
    return encrypted

def caesarDecrypt(message, key=0):
    # Initialize decrypted string
    decrypted = ""

    for i in range(len(message)):
        char = message[i]

        if (65 <= ord(char) <= 90):     # Check for uppercase 
            decrypted += chr(65 + (ord(char) - 65 - key) % 26)
        elif (97 <= ord(char) <= 122):  # Check for lowercase
            decrypted += chr(97 + (ord(char) - 97 - key) % 26)
        else:                           # Every other symbol
            decrypted += char
    return decrypted
