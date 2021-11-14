class Node:
    values = []
    
    def __init__(self, data):
        self.big = None
        self.too_big = None
        self.small = None
        self.data = data
        
    def insert(self, data):
        if self.data:
            if data-self.data >= 10:
                if self.too_big is None:
                    self.too_big = Node(data)
                else:
                    self.too_big.insert(data)
            elif data-self.data >= 0:
                if self.big is None:
                    self.big = Node(data)
                else:
                    self.big.insert(data)
            else:
                if self.small is None:
                    self.small = Node(data)
                else:
                    self.small.insert(data)
        else:
            self.data = data
            
    def delete(self, data):
        self.empty()
        self.traversal(printvalue = False)
        
        self.big = None
        self.too_big = None
        self.small = None
        self.data = None
        
        for i in self.values:
            if i != data:
                self.insert(i)
           
    def traversal(self, printvalue = True):
        if self.small:
            self.small.traversal(printvalue)
        if printvalue:
            print(self.data)
        self.values.append(self.data)
        if self.big:
            self.big.traversal(printvalue)
        if self.too_big:
            self.too_big.traversal(printvalue)
    
    def empty(self):
        if self.values != None:
            for i in range(len(self.values)):
                self.values.pop()