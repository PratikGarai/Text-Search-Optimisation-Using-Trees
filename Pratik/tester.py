from Content import FullText
from Trie import Trie


def main():

    # declarations of the structures
    ob_text = None
    ob_trie = Trie()

    # reading an inputing the file
    with open("test.txt", "r") as t:
        text = t.read()
        print(text)
        ob_text = FullText(text, ob_trie)

    # validation of structure construction
    print("\n Text Added! Now launching printAll() \n")
    print("S.no.\tW.no.\tBeg.\tEnd\tContent")
    ob_text.printAll()
    print("\n Now analysing the generated \n")
    ob_trie.printAll()

    # validation of structure functionality
    print("Number of search queries : ", end = "")
    n = int(input())
    for i in range(n):
        print("Query",(i+1),": ", end="")
        q = input()
        res = ob_trie.findLocations(q)
        if res[0]:
            print("Node exists . Number of ending : ", res[1])
        else:
            print("Node doesn't even exist")

if __name__=='__main__':
    main()
