####Swap the nodes
#http://www.codeskulptor.org/#user40_9safm082BXzcoX2.py
#http://www.codeskulptor.org/#user40_PIjJJGs8U3cUfUd_1.py

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
    
    def prnt(self, head):
        temp = head
        while(temp):
            print temp.datum
            temp = temp.n
            
#  def search(self,head,numbertofind):
#        temp = head 
#        if temp == None:
#            return False
#        else:    
#            if temp.datum == numbertofind:
#                return True
#            else:
#                temp = temp.n
#                return self.search(temp, numbertofind) 

    def swap (self, head, value1, value2):
        
        counter =0
        
        temp = head # This head aint just head: it's a node as made in 3rd line of push function. Hence you can access the 
        print ' First Value to find ', value1 ,' Second Value to find ', value2
        while(temp):
            if temp.datum == value1 or temp.datum == value2:
                if temp.datum == value1:
                    x = temp # temp.n is a node itself
                    if counter ==0:
                        xx= None
                    else:
                        xx=AA
                    print "Node's value which is matched", x.datum
                else:
                    y = temp 
                    if counter ==0:
                        yy= None
                    else:
                        yy=AA
                    print "Node's value which is matched", y.datum
            else:
                print "neither of the values matched the present LL node"
                AA = temp
                counter += 1
                print "store this node's value to repserent ", AA.datum
           
            
            temp = temp.n
        
        t=x.n
        x.n=y.n
        y.n=t
        if xx==None:
            self.head = y    
        else:
            xx.n = y
        if yy==None:
            self.head = x    
        else:
            yy.n = x
        
        
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
    print "LL head is", L.head.datum
    L.prnt(L.head)
    L.swap( L.head,34,67)
    print "LL head is", L.head.datum
    L.prnt(L.head)
    
 
    
    
    
   