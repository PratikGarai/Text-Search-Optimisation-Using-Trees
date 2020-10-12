from Content import FullText
from Trie import Trie

class Document():

    def __init__(self, text):
        self.ob_trie = Trie()
        self.ob_text = FullText(text, ob_trie)


    def printAllContent(self):
        self.ob_text.printAll()


    def printAllTrie(self):
        self.ob_trie.printAll()


    def search(self, word):
        res = ob_trie.findLocations(word)
        return res


    def suggestions(self, substring):
        res = ob_trie.getAutoCompleteSuggestions(substring)
        return res
