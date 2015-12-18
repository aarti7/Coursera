# to find a value in a simple Binary Tree
#http://www.codeskulptor.org/#user40_RpwokI8ckJ_0.py

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left      = Node(2);
root.left.left  = Node(4);
root.left.right  = Node(5);

root.right     = Node(3);
root.right.left  = Node(6);
root.right.right  = Node(7);


#def Bin_tree_search( rooty, value_to_find):
#    temp = rooty
#    
#    if temp == None:
#        #print "reached the leaf/dead end"
#        return
#    else:
#        if temp.val == value_to_find:
#            print " value found"
#        else:
#            Bin_tree_search (temp.left, value_to_find)
#            Bin_tree_search (temp.right, value_to_find)
#            return
#            
#    
#Bin_tree_search (root, 15)

##############################
#
# how to make the program tell you that the value_to_find was not there in the tree:
#
# What if the program only tells you that always, except one exception where the value is matched!!
#
#
##############################


def search( rooty, value_to_find):
    temp = rooty
    if temp == None: 
        return False
        pass
    else:
        if not temp.val == value_to_find:
            left_result   = search (temp.left, value_to_find)
            right_result  = search (temp.right, value_to_find)
            return left_result or right_result
        else:
            return True

print search (root, 15)



















