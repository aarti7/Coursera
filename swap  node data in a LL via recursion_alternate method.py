####swap  node data in a LL via recursion
#http://www.codeskulptor.org/#user40_9safm082BXzcoX2.py
#http://www.codeskulptor.org/#user40_gE5q0ULgKrYK8Op.py
#http://www.codeskulptor.org/#user40_Mcz8HTc7zXbMQHM.py


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
        tempi = head
        while(tempi):
            print tempi.datum
            tempi = tempi.n

    def swap (self, head, value1, value2):
        
        counter =0
        
        temp = head # This head aint just head: it's a node as made in 3rd line of push function. Hence you can access the 
        print ' value1 ', value1 ,' Value2 ', value2
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
                AA=temp
            
            else:
                print "neither of the values matched the present LL node"
                AA = temp # store the current temp value before its changed at the end of the loop. You will need it to know the previous node pointer 
                counter += 1
                print "store this node's value to repserent ", AA.datum
           
            
            temp = temp.n
            # After this we go outside while loop
           
        
        # to check if the value is the 'first-node' itself or not
        if xx==None:
            self.head = y    # it is; hence in this line we are changing the head to the 2nd value
        else:
            xx.n = y         # is not! in that case, the node(gpt by previous node pointer i.e. = xx.n) will be assigned to y
        
        if yy==None:		#
            self.head = x   # this is the same code as above just for reveresed order to y n x
        else:				#
            yy.n = x		#
        
        ####MAJOR ACHIEVEMENT######
        ####
        if x.n == y or y.n ==x: # check if they are adjacent! this is the loop when they are!!!
            if x.n ==y:			# x is pointing to y
                y.n = x 		#hence you reverse them!!
            else: 				#else (means x is not pointing to y or in othere words: y.n ==x is true, ie y is potintin gto x)
                x.n = y 		#hence you reverse them!!
        else: 	# if not adjacent
            t=x.n
            x.n=y.n			# simple swapping
            y.n=t

            
         
        
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
    L.swap( L.head,34,3)
    print "LL head is", L.head.datum
    L.prnt(L.head)
    
 
    
    
    
   
