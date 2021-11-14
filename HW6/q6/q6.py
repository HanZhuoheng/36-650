class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None
        
class ReversedLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail
        
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")
        
    def insert(self, data):
        node = Node(data)
        current = self.tail
        node.previous = current
        self.tail = node
        
    def delete(self, data):
        if not self.tail:
            return

        temp = self.tail

        if self.tail.data == data:
            tail = temp.previous
            return 

        while temp.previous:
            if temp.previous.data == data:
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        return
    
    def search(self, data):
        temp = self.tail

        while temp:
            if temp.data == data:
                return True
            
            temp = temp.previous
        return False