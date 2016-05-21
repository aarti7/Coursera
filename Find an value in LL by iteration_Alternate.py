#### Find an value in LL by iteration####
###http://www.codeskulptor.org/#user41_3N38bL2d4sP2MKw_0.py
class Node:
    def __init__(self, value):
        self.datum = value  											
        self.next = None  										
class LinkedLis:
    def __init__(self):
        self.head = None 											
           
    def push(self, newdata): 									
        addednode = Node(newdata) 								
        addednode.next = self.head 								
        self.head = addednode										

def find(head, valuetofind):
    temp = head
    while(temp):
        if temp.datum == valuetofind:
            return True
        else:
            #print valuetofind, "doesn't match", temp.datum
            temp = temp.next
    return False          
            
if __name__=='__main__':
    L = LinkedLis()
    L.push(3)
    L.push(34)
    L.push(134)
    print find(L.head,31)   
