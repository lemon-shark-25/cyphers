import random

class SubstitutionCypher:
    def __init__(self):
        self._alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        self._encryptKey = self.genEncryptKey()
        self._encryptCypher, self._decryptCypher = {}, {}
        self.genCyphers(self._encryptKey)

    def getKey(self):
        return self._encryptKey

    def setKey(self, text):
        self._encryptKey = text.upper()
        self.genCyphers(self._encryptKey)

    def genEncryptKey(self):
        shuffled = self._alphabet[:]
        random.shuffle(shuffled)
        return ''.join(shuffled)

    def isValidKey(self, key):
        key_chars = list(key.upper())
        alphabet_set = set(self._alphabet)
        if len(key_chars) != len(self._alphabet):
            return False
        return set(key_chars) == alphabet_set

    def genCyphers(self, key):
        enCypher = {}
        deCypher = {}
        for original, substitute in zip(self._alphabet, key):
            enCypher[original] = substitute
            deCypher[substitute] = original
        self._encryptCypher = enCypher
        self._decryptCypher = deCypher

    def subsEncrypt(self, text):
        result = "" 
        for c in text:
            if c.isupper():
                result += self._encryptCypher.get(c, c)
            elif c.islower():
                result += self._encryptCypher.get(c.upper(), c).lower()
            else:
                result += c
        return result

    def subsDecrypt(self, text):
        result = ""
        for c in text:
            if c.isupper():
                result += self._decryptCypher.get(c, c)
            elif c.islower():
                result += self._decryptCypher.get(c.upper(), c).lower()
            else:
                result += c
        return result

