####Add a number to all the data values of nodes in a LL
#http://www.codeskulptor.org/#user40_vpnKxpcdpy_0.py

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


def addtoLL(head, addnum):
    temp= head
    while(temp):
        temp.datum = temp.datum + addnum
        temp = temp.n
        
            
if __name__=='__main__':
    L = LinkedLis()
    L.push(3)
    L.push(34)
    L.push(134)
    addtoLL(L.head, 5)
    print L.head.datum