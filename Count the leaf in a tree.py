# Count the  leaf in a tree
#http://www.codeskulptor.org/#user40_mF7DLeKJ5SKT1Pf.py
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
#root.right.right.right  = Node(8);


def Countleaf(root):
    temp = root
    if not temp:
        return 0
    else:
        a=Countleaf(temp.left)
        b=Countleaf(temp.right)
    
        if a==0 and b==0:
            return 1
        else:
            return a+b

        
print Countleaf(root)

