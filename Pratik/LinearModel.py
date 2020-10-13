class LinearModel():

    def __init__(self, text):
        self.text = text

    def search(self, word):
        s = ''
        c,w,l = 0,0,0
        address = []
        for i in self.text :
            if i==' ':
                w += 1
            if i=='\n':
                l += 1
                w = 0
            if i==' ' or i=='\n':
                s = ''
            else :
                s += i
                if s==word:
                    c += 1
                    address.append([l,w])
        return address
