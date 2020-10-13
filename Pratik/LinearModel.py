class LinearModel():

    def __init__(self, text):
        self.text = text

    def search(self, word):
        s = ''
        c,w,l,beg = 0,0,0,0
        le = len(word)
        address = []
        for i in self.text :
            if i==' ':
                w += 1
                beg += 1
            if i=='\n':
                l += 1
                w = 0
                beg = 0
            if i==' ' or i=='\n':
                s = ''
            else :
                s += i
                beg += 1
                if s==word:
                    c += 1
                    address.append([l,w,beg-le,beg])
        return address
