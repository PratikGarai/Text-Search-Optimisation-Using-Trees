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
        # print("Adding : ",word,"...")
        current = self.head
        for i in word :
            current = current.moveToChild(i)
        current.addAddress(word_pointer)
        current.setEnding()

    def findLocations(self, word):
        current = self.head
        for i in word:
            try : 
                current = current.children[i]
            except :
                return (False,[], None)
        return (True, self.get_terminals(current), current)

    def getAutoCompleteSuggestions(self, word):
        res = self.findLocations(word)
        if not res[0]:
            return []
        nodes = [res[2]]
        suggestions = []
        while nodes!=[]:
            node = nodes.pop(0)
            if node.is_ending :
                suggestions.append(node.addresses[0].content)
            nodes.extend(node.children.values())
        return suggestions

    def get_terminals(self, ob):
        if ob.is_ending:
            terminals = [ob]
        else :
            terminals = []
        nodes = [ob]
        while(nodes!=[]):
            curr = nodes.pop(0)
            children = curr.children.values()
            terminals.extend(list(filter(lambda x : x.is_ending, children)))
            nodes.extend(children)
        terminals_addresses = []
        for i in terminals:
            terminals_addresses.extend(i.addresses)
        return terminals_addresses

    def printAll(self):
        print("\nAll stuff of trie printed\n")
        print("Level\tAlpha\tEnd\tN_end\tChildren")
        alphabets = [self.head]
        while(alphabets!=[]):
            current = alphabets.pop(0)
            print(current.level, current.alphabet, current.is_ending, len(current.addresses), current.children.keys(), sep="\t")
            alphabets.extend(current.children.values())
        print()
