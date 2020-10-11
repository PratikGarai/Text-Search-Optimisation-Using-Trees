from Content import FullText
from Trie import Trie

def main():
    ob_text = None
    ob_trie = Trie()
    with open("test.txt", "r") as t:
        text = t.read()
        print(text)
        ob_text = FullText(text)
    print("\n Text Added! Now launching printAll() \n")
    print("S.no.\tW.no.\tBeg.\tEnd\tContent")
    ob_text.printAll()

if __name__=='__main__':
    main()
