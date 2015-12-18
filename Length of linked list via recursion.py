### Length of linked list via recursion ###
#url: http://www.codeskulptor.org/#user40_4xo15VhpPp_3.py
# important points: 
#.next is an inbuilt command in python
# None = Null value in python

class Node:
    def __init__(self, data):
        self.data = data  										# Assign data
        self.next = None  										# Initialize next as null

class LinkedList:
    def __init__(self):
        self.head = None 										# its initial value is NULL: ie the list length is zero
    
    def push(self, newdata): 									# When you push new node, you put new data in 
        newnode = Node(newdata) 								# you CREATE a new node from scratch; it will get all featues f the classs 'NODE'
        newnode.next = self.head 								# you move the head backward by pointing new node to head such that old head is now secind and new node is first
        self.head = newnode										# you assign new node as new head of the old LL
 
    def length(self, nn):
        if  not nn: # ie if (not nn) = true; ie if nn = false, or in case of python, its  null or none
                    # this is the base case: it'll happen only when we reach head
                    # head is the only node that points to null
                    # in recursive, we keep shortening the original list after every step/count such that we treat thet last node as a LL with only one node.
            return 0
        else:
            return 1 + self.length(nn.next)
          

if __name__=='__main__':
    L = LinkedList()
    print L.length(L.head)
    L.push(3)
    print L.length(L.head)
    