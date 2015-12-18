#how to detect a loop in LL
#http://www.codeskulptor.org/#user40_Va0dwFNj0s_0.py

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
                
                return
    def detectloop(self):
        temp = self.head
        slow = temp
        fast = temp
        while(temp):
            slow = slow.n
            if fast == None or fast.n ==None:
                return "no loop founnd here"
            else:
                fast = fast.n.n
            
            temp = temp.n
            
            if slow == fast:
                return "there is a loop"
            else:
                pass
            
        
            
            
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
    #L.reverse_list(L.head)
    print "new head", L.head.datum
    print L.detectloop()
    
    
