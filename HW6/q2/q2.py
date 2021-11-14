class Queue:
    inner_list = []
    
    def enqueue(self, value):
        self.inner_list.append(value)
        return self.inner_list
        
    def dequeue(self):
        return self.inner_list.pop(0)
    
    def delete(self, value):
        j = 0
        for i in range(len(self.inner_list)):
            if self.inner_list[i-j] != value:
                self.enqueue(self.inner_list[i-j])
                self.dequeue()
                j+=1
            else:
                self.dequeue()
                j+=1          
        return self.inner_list