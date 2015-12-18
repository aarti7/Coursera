#http://www.codeskulptor.org/#user40_4v0gWipiq9_0.py
# The size of the tree

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



def sizeoftree(root_t):
    temp = root_t
    if not temp==None:
        s = sizeoftree(temp.left)
        ss = sizeoftree(temp.right)
        return s+ss+1 # 1 is to add the node you are at!
    else:
        return 0
        
    
print sizeoftree(root)