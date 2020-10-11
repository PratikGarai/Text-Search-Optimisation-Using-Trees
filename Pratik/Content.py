class Word():

    def __init__(self, word, number, begin, length):
        self.content = word
        self.number = number
        self.address_begin = begin
        self.address_end = begin+length

    def printAll(self):
        print(self.number, self.address_begin, self.address_end, self.content, sep="\t") 


class Sentence():

    def __init__(self, sentence, number):
        self.words = []
        self.number = number
        count = 0
        for num, i in enumerate(sentence.split()):
            l = len(i)
            self.words.append(Word(i, num, count , l ))
            count += l+1

    def printAll(self):
        for i in self.words:
            print(self.number, end="\t")
            i.printAll()


class FullText():

    def __init__(self, text):
        self.sentences = []
        for num,i in enumerate(text.split("\n")):
            self.sentences.append(Sentence(i, num))

    def printAll(self):
        for i in self.sentences :
            i.printAll()
