from LinearModel import LinearModel
import time

def main():

    FILE_NAME = "test2.txt"
    lin = None

    # setups
    with open(FILE_NAME, "r") as t :
        text = t.read()
        a = time.time_ns()
        lin = LinearModel(text)
        b = time.time_ns()
        print("Model initialised in : ",(b-a),"s")

    # printer methods
    def search_results_printer(res):
        if len(res):
            print("Node exists . Addresses : " )
            print("S.no.\tW.no.\tBeg.\tEnd")
            for i in res:
                print(i[0], i[1], i[2], i[3], sep='\t')
        else:
            print("Node doesn't exist")

    def autocomplete_results_printer(res):
        if res==[]:
            print("No suggestions")
        else:
            print("Num.\tSuggestion")
            for num, i in enumerate(res):
                print(num+1,i,sep="\t")


    # user inputs
    print("\nEnter the number of search queries : ", end="")
    n_searches  = int(input())
    for i in range(n_searches):
        print("Enter the",(i+1),"query : ", end="")
        q = input()
        a = time.time_ns()
        res = lin.search(q)
        b = time.time_ns()
        print("\n",len(res),"results fetched in :",(b-a),"ns")
        print("Do you want to print the results? (y for yes, else no)")
        inp = input()
        if inp=='y' or inp=='Y':
            print("\nResults :")
            search_results_printer(res)

    print("\nEnter the number of autocomplete queries : ", end="")
    n_searches  = int(input())
    for i in range(n_searches):
        print("Enter the",(i+1),"query : ", end="")
        q = input()
        a = time.time_ns()
        res = lin.suggester(q)
        b = time.time_ns()
        print("\n",len(res),"results fetched in :",(b-a),"ns")
        print("Do you want to print the results? (y for yes, else no)")
        inp = input()
        if inp=='y' or inp=='Y':
            print("\nResults :")
            autocomplete_results_printer(res)

if __name__=='__main__':
    main()
