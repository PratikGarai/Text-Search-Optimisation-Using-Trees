from Content import FullText

def main():
    ob = None
    with open("test.txt", "r") as t:
        text = t.read()
        print(text)
        ob = FullText(text)
    print("\n Text Added! Now launching printAll() \n")
    print("S.no.\tW.no.\tBeg.\tEnd\tContent")
    ob.printAll()

if __name__=='__main__':
    main()
