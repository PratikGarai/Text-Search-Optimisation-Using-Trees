from Content import FullText
from Trie import Trie
from Document import Document
from LinearModel import LinearModel
import time

def test(f_name):

    # declarations of the structures
    doc = None

    # reading an inputing the file
    with open(f_name, "r") as t:
        text = t.read()
        print(text)
        doc = Document(text)
        lin = LinearModel(text)

    # validation of structure construction
    # print("\n Text Added! Now launching printAll() \n")
    # print("S.no.\tW.no.\tBeg.\tEnd\tContent")
    # doc.printAllContent()
    # print("\n Now analysing the generated \n")
    # doc.printAllTrie()

    # validation of structure functionality

    def search_results_printer(res):
        if len(res):
            print("Node exists . Addresses : " )
            print("S.no.\tW.no.\tBeg.\tEnd")
            for i in res:
                print(i[0], i[1], i[2], i[3], sep='\t')
        else:
            print("Node doesn't exist")

    print("Number of search queries : ", end = "")
    n = int(input())
    for i in range(n):
        print("Query",(i+1),": ", end="")
        q = input()
        print("\nDocument model results\n------------")
        a = time.time()
        res1 = doc.search(q)
        search_results_printer(res1)
        b = time.time()
        print("Time : ",b-a)
        print("\nLinear model results\n------------")
        c = time.time()
        res2 = lin.search(q)
        search_results_printer(res2)
        d = time.time()
        print("Time : ",d-c)

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
    test("test1.txt")
