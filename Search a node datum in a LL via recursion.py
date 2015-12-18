####Search a node datum in a LL via recursion
#http://www.codeskulptor.org/#user40_9safm082BXzcoX2.py

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

        
    def search(self,head,numbertofind):
        temp = head 
        if temp == None:
            return False
        else:    
            if temp.datum == numbertofind:
                return True
            else:
                temp = temp.n
                return self.search(temp, numbertofind)
            
            
if __name__=='__main__':
    L = LinkedLis()
    L.push(3)
    L.push(34)
    L.push(134)
    print L.search(L.head,3)