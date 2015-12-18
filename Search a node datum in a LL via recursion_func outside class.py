class Node:
    def __init__(self, value):
        self.datum = value  											
        self.n = None  										

class LinkedLis:
    def __init__(self):
        self.head = None 											
           
    def push(self, newdata): 									
        addednode = Node(newdata) 								
        addednode.n = self.head 								
        self.head = addednode										

def find(head, valuetofind):
    temp = head
    if temp == None:
        return False
    else:
        if temp.datum == valuetofind:
            return True
        else:
            return find(temp.n, valuetofind)
    
        
        
            
if __name__=='__main__':
    L = LinkedLis()
    L.push(3)
    L.push(34)
    L.push(134)
    print find(L.head, 4)    