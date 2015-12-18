#### program to print a LL elements
#http://www.codeskulptor.org/#user40_kO2x3pN4oLgvrnP.py

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
    
    def prnt(self, head):
        temp = head
        while(temp):
            print temp.datum
            temp = temp.n
            

if __name__=='__main__':
    L = LinkedLis()
    L.push(3),L.push(34),L.push(134),L.push(67)
    L.prnt(L.head)
    
    
    
    
   