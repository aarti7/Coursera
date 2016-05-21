#### Find a value in LL by iteration####
###http://www.codeskulptor.org/#user41_a5uUab9vxMoqaWS_0.py


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
        
    def find(self, valuetofind):
        temp = self.head
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
    print L.find(3)    
