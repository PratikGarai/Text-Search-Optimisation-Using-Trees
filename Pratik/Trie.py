class Alphabet():

    def __init__(self, alphabet, level):
        self.alphabet = alphabet
        self.children = {}
        self.is_ending = False
        self.level = level
        self.addresses = []

    def moveToChild(self, character):
        try :
            return self.children[character]
        except :
            self.children[character] = Alphabet(character, self.level+1)
            return self.children[character]

    def setEnding(self):
        self.is_ending = True

    def addAddress(self, instance):
        self.addresses.append(instance)


class Trie():

    def __init__(self):
        self.head = Alphabet('', 0)

    def add(self, word, word_pointer):
        print("Adding : ",word,"...")
        current = self.head
        for i in word :
            current = current.moveToChild(i)
        current.setEnding()
        current.addAddress(word_pointer)

    def printAll(self):
        print("\nAll stuff of trie printed\n")
        alphabets = [self.head]
