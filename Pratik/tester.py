from Content import FullText
from Trie import Trie
from Document import Document

def main():

    # declarations of the structures
    doc = None

    # reading an inputing the file
    with open("test.txt", "r") as t:
        text = t.read()
        print(text)
        # ob_text = FullText(text, ob_trie)
        doc = Document(text)

    # validation of structure construction
    print("\n Text Added! Now launching printAll() \n")
    print("S.no.\tW.no.\tBeg.\tEnd\tContent")
    doc.printAllContent()
    print("\n Now analysing the generated \n")
    doc.printAllTrie()

    # validation of structure functionality
    print("Number of search queries : ", end = "")
    n = int(input())
    for i in range(n):
        print("Query",(i+1),": ", end="")
        q = input()
        res = doc.search(q)
        if res[0]:
            print("Node exists . Number of ending : ", res[1])
        else:
            print("Node doesn't even exist")

    print("Number of autocomplete queries : ", end = "")
    n = int(input())
    for i in range(n):
        print("Query",(i+1),": ", end="")
        q = input()
        res = doc.suggestions(q)
        if res!=[]:
            print("Suggestions ", res)
        else:
            print("No suggestions")


if __name__=='__main__':
    main()
