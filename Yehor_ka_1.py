class VigenereCipher(object):

    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.MoveNumbers = []
        for i in key:
            self.MoveNumbers.append(alphabet.index(i))

    def encode(self, text):
        result = []
        n = 0
        for symbol in text:
            if symbol in self.alphabet:
                indexforlist = n
                while indexforlist >= len(self.MoveNumbers):
                    indexforlist -= len(self.MoveNumbers)
                    
                index = self.alphabet.index(symbol) + self.MoveNumbers[indexforlist]
                while index >= len(self.alphabet):
                    index -= len(self.alphabet)
                    
                result.append(self.alphabet[index])
            else:
                result.append(symbol)
            n += 1
        return(''.join(result))

    def decode(self, text):
        result = []
        n = 0
        for symbol in text:
            if symbol in self.alphabet:
                indexforlist = n
                while indexforlist >= len(self.MoveNumbers):
                    indexforlist -= len(self.MoveNumbers)

                index = self.alphabet.index(symbol) - self.MoveNumbers[indexforlist]
                while index >= len(self.alphabet):
                    index -= len(self.alphabet)

                result.append(self.alphabet[index])
            else:
                result.append(symbol)
            n += 1
        return (''.join(result))
