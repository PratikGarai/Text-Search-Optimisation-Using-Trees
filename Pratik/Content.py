class FullText():

    class Sentence():

        class Word():

            def __init__(self, word, number, begin, length, TRIE_OBJ):
                self.content = word
                self.number = number
                self.address_begin = begin
                self.address_end = begin+length
                TRIE_OBJ.add(word, self)

            def printAll(self):
                print(self.number, self.address_begin, self.address_end, self.content, sep="\t") 

        def __init__(self, sentence, number, TRIE_OBJ):
            self.words = []
            self.number = number
            count = 0
            for num, i in enumerate(sentence.split()):
                l = len(i)
                self.words.append(self.Word(i, num, count , l, TRIE_OBJ))
                count += l+1

        def printAll(self):
            for i in self.words:
                print(self.number, end="\t")
                i.printAll()

    def __init__(self, text, trie_obj):
        self.TRIE_OBJ = trie_obj
        self.sentences = []
        for num,i in enumerate(text.split("\n")):
            self.sentences.append(self.Sentence(i, num, self.TRIE_OBJ))

    def printAll(self):
        for i in self.sentences :
            i.printAll()
