# Basic impolementation of TRIE data structure

class Alphabet:
    def __init__(self, data, level, address_end):
        self.data = data
        self.successors = {}
        self.level = level
        self.ending = False
        self.end_pos = [address_end]

    def check_succeessor(self, alphabet):
        if alphabet in self.successors :
            return True
        return False

    def add_successor(self, alphabet, level, address):
        self.successors[alphabet] = Alphabet(alphabet,level, address)

    def get_successor(self,alphabet):
        if self.check_succeessor(alphabet):
            return self.successors[alphabet]
        return None

    def get_successors_dict(self):
        return self.successors

    def set_as_ending(self):
        self.ending = True

    def is_ending(self):
        return self.ending

    def get_end_pos(self):
        return self.end_pos

    def get_highlightings(self):
        return [(i[0], i[1]-self.level, i[1]) for i in self.end_pos]
    
    def add_address(self, address):
        self.end_pos.append(address)

class Trie:
    def __init__(self):
        self.head = Alphabet('',0,(0,0))
    
    def add_word(self, word, address_begin):
        current = self.head
        for index,i in enumerate(word) :
            if not current.check_succeessor(i):
                current.add_successor(i, index+1, (address_begin[0], address_begin[1]+index+1))
            else :
                current.add_address((address_begin[0], address_begin[1]+index))
            current = current.get_successor(i)
        current.set_as_ending()
        print(word,"\t\t\t added")

    def get_all_subnodes(self, string, node):
        ls1 = {}
        for i,j in node.get_successors_dict().items():
            ls1[string+i] = j
            ls2 = self.get_all_subnodes(string+i, j)
            ls1.update(ls2)
        return ls1

    # return a list of auto-complete suggestions based on the typed strings
    def get_suggestions(self, string): 
        current = self.head
        for i in string:
            current = current.get_successor(i)
            if not current:
                return []
        return dict(filter( lambda x : x[1].is_ending() , self.get_all_subnodes(string, current).items()))

    def highlight(self, string):
        current = self.head
        for i in string:
            current = current.get_successor(i)
            if not current:
                return []
        return current.get_highlightings()
    
    #### TEST METHODS HERE ####
    # text-based visualisation function (test)
    def checker(self):
        def printer(prefix, node,ending):
            if not ending:
                ending = ''
            print('Successors of "',prefix,'"\t\t\t : ',str(list(node.get_successors_dict().keys())),'\t\t\t',ending,sep="")
            for i,j in node.get_successors_dict().items():
                printer(prefix+i, j, j.is_ending())
        printer('',self.head, False)


#testing function
def test(choice):
    trie = Trie()
    text = "Hello Halo Helo My Mine Type Typ Typo"
    print(text)
    ptr = 0
    for i in text.strip().split() :
        trie.add_word(i,(0,ptr))     # 0th line and ptr th character
        ptr += len(i)+1
    print()

    if choice==1:
        # Test 1 : check the structure generation
        trie.checker()
        return

    if choice==2:
        #Test 2 :  check the autocomplete generation
        print('Enter the term to generate autocomplete suggestions for')
        st = input()
        sug = trie.get_suggestions(st)
        if sug==[]:
            print("No valid suggestions")
            return
        for index,i in enumerate(sug.items()):
            print(index,'\t',i[0],'\t',i[1])

    if choice==3:
        #Test 3:  check for highlight generation
        print('Enter the pattern to search positions for')
        pt = input()
        positions = trie.highlight(pt)
        print()
        if positions==[]:
            print('No valid suggestions found')
            return
        for i in positions :
            print(i[0],'\t',i[1],'\t',i[2])
        return

def main():
    pass

if __name__=='__main__':
    test(2)
