# Basic impolementation of TRIE data structure

class Alphabet:
    def __init__(self, data):
        self.data = data
        self.successors = {}

    def check_succeessor(self, alphabet):
        if alphabet in self.successors :
            return True
        return False

    def add_successor(self, alphabet):
        self.successors[alphabet] = Alphabet(alphabet)
