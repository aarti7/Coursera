# How to reverse a Linked list via recursion
#http://www.codeskulptor.org/#user40_7noL5qyU1T_0.py


class NNode:
    def __init__(self, value):
        self.datum = value  											
        self.n = None  										

class LinkedLis:
    def __init__(self):
        self.head = None 											
           
    def push(self, newdata): 									
        addednode = NNode(newdata) 								
        addednode.n = self.head 								
        self.head = addednode
    
    def prnt(self):
        tempi = self.head
        while(tempi):
            print tempi.datum
            tempi = tempi.n

    def reverse_list(self,head):
            temp = head
            if temp.n==None:
                self.head=temp 						# you make the head the last node: temp was holding the value
                return
            else:
                self.reverse_list(temp.n)
                temp.n.n=temp
                temp.n = None
                return

if __name__=='__main__':
    L = LinkedLis()
    L.push(3)
    L.push(34)
    L.push(134)
    L.push(2)
    L.push(67)
    L.push(5)
    L.push(89)
    print "< 89, 5 , 67, 2, 134, 34, 3>"
    print "Old head", L.head.datum
    L.prnt()
    L.reverse_list(L.head)
    print "new head", L.head.datum
    L.prnt()
    