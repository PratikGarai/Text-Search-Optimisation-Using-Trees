# Basic impolementation of TRIE data structure

class Alphabet:
    def __init__(self, data, level):
        self.data = data
        self.successors = {}
        self.level = 0
        self.ending = False

    def check_succeessor(self, alphabet):
        if alphabet in self.successors :
            return True
        return False

    def add_successor(self, alphabet, level):
        self.successors[alphabet] = Alphabet(alphabet,level)

    def get_successor(self,alphabet):
        return self.successors[alphabet]

    def get_successors_dict(self):
        return self.successors

    def set_as_ending(self):
        self.ending = True

    def is_ending(self):
        return self.ending

class Trie:
    def __init__(self):
        self.head = Alphabet('',0)
    
    def add_word(self, word):
        current = self.head
        for index,i in enumerate(word) :
            if not current.check_succeessor(i):
                current.add_successor(i, index+1)
            current = current.get_successor(i)
        current.set_as_ending()
        print(word,"\t\t\t added")

    # text-based visualisation function (test)
    def checker(self):
        def printer(prefix, node,ending):
            if not ending:
                ending = ''
            print('Successors of "',prefix,'"\t\t\t : ',str(list(node.get_successors_dict().keys())),'\t\t\t',ending,sep="")
            for i,j in node.get_successors_dict().items():
                printer(prefix+i, j, j.is_ending())
        printer('',self.head, False)

    def get_suggestions(self, string): 
        pass

#testing function
def test():
    trie = Trie()
    text = "Hello Halo Helo My Mine Type Typ Typo"
    print(text)
    for i in text.strip().split() :
        trie.add_word(i)
    print()
    trie.checker()

def main():
    pass

if __name__=='__main__':
    test()
