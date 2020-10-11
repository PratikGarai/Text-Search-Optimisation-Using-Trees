class Word():

    def __init__(self, word):
        self.content = []
        self.number = None
        self.address_begin = None
        self.address_end = None


class Sentence():

    def __init__(self, sentence):
        self.words = []
        self.number = None


class FullText():

    def __init__(self, text):
        self.sentences = []
