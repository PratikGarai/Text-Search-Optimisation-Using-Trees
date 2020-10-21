from  Document import Document
import time

def main():

    FILE_NAME = "test2.txt"
    doc = None

    # setups
    with open(FILE_NAME, "r") as t :
        text = t.read()
        a = time.time_ns()
        doc = Document(text)
        b = time.time_ns()
        print("Model initialised in : ",(b-a)/10**9,"s")

    # printer methods
    def search_results_printer(res):
        if len(res):
            res, l = res[0], res[1]
            print("Node exists . Addresses : " )
            print("S.no.\tW.no.\tBeg.\tEnd")
            for i in res:
                print(i.s_number, i.number, i.address_begin, i.address_begin+l, sep='\t')
            print(len(res),"results fetched.")
        else:
            print("Node doesn't exist")

    def autocomplete_results_printer(res):
        if res==[]:
            print("No suggestions")
        else:
            print("Num.\tSuggestion")
            for num, i in enumerate(res):
                print(num+1,i,sep="\t")
            print(len(res),"results fetched.")


    # user inputs
    print("Enter the number of search queries : ", end="")
    n_searches  = int(input())
    for i in range(n_searches):
        print("Enter the",(i+1),"query : ", end="")
        q = input()
        a = time.time_ns()
        res = doc.search(q)
        b = time.time_ns()
        print("\nResults :")
        search_results_printer(res)
        print("\nResults fetched in :",(b-a),"ns")

    print("Enter the number of autocomplete queries : ", end="")
    n_searches  = int(input())
    for i in range(n_searches):
        print("Enter the",(i+1),"query : ", end="")
        q = input()
        a = time.time_ns()
        res = doc.suggestions(q)
        b = time.time_ns()
        print("\nResults :")
        autocomplete_results_printer(res)
        print("\nResults fetched in :",(b-a),"ns")

if __name__=='__main__':
    main()
