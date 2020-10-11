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

    def findLocations(self, word):
        current = self.head
        for i in word:
            try : 
                current = current.children[i]
            except :
                return (False,[])
        return (True, len(current.addresses))

    def getAutoCompleteSuggestions(self, word):
        pass

    def printAll(self):
        print("\nAll stuff of trie printed\n")
        print("Level\tAlpha\tEnd\tN_end\tChildren")
        alphabets = [self.head]
        while(alphabets!=[]):
            current = alphabets.pop(0)
            print(current.level, current.alphabet, current.is_ending, len(current.addresses), current.children.keys(), sep="\t")
            alphabets.extend(current.children.values())
        print()
