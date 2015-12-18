# Find depth of a tree
#http://www.codeskulptor.org/#user40_4iNFTSdEdoHttLb.py

class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

root = Node(1)
root.left      = Node(2);
#root.left.left  = Node(4);
#root.left.right  = Node(5);

root.right     = Node(3);
#root.right.left  = Node(6);
root.right.right  = Node(7);
root.right.right.right  = Node(8);


## Noob code
#def depth(root_tt):
#    temp = root_tt
#    if temp.left == None and temp.right == None:
#        return 1
#    else: 									# i.e. you CAN go either right or left
#        if temp.left:
#            x = depth(temp.left)
#        else:
#            x=0
#        if temp.right:
#            y = depth(temp.right)
#        else:
#            y=0
#    return max(x+1,y+1)
#    
#print depth(root)


def depth (root_tt):
    temp = root_tt
    if not temp:
        return 0
    else:
        x= depth(temp.left)
        y= depth(temp.right)
        return max(x+1, y+1)
    
print depth(root)