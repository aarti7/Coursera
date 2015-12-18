#### Find an value in LL by iteration####
###http://www.codeskulptor.org/#user40_3i4PzDsfdR_3.py
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

    while(temp):
        if temp.datum == valuetofind:
            #print True
            return True

        else:
            print valuetofind, "doesn't match", temp.datum
            temp = temp.n
    return False          
            
if __name__=='__main__':
    L = LinkedLis()
    L.push(3)
    L.push(34)
    L.push(134)
    print find(L.head.n,3)    