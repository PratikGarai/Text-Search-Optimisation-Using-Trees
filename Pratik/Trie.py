class Alphabet():

    def __init__(self, alphabet, level, is_ending):
        self.alphabet = alphabet
        self.children = {}
        self.is_ending = is_ending
        self.level = level


class Trie():

    def __init__(self):
        self.head = Alphabet('', 0, False)
