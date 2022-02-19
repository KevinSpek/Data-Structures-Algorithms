

from trees.Tree import Tree
from trees.TreeNode import TreeNode

class BinaryTree(Tree):
    
    def __init__(self):
        super(BinaryTree, self).__init__()
        

    
    def insert(self, value):
        newNode = TreeNode(value)
        if self.getRoot() is None:
            self.setRoot(newNode)
            return
        
        temp = self.getRoot()
        while True:
            if value < temp.getValue() and temp.getLeft() is not None:
                temp = temp.getLeft()
            elif value >= temp.getValue() and temp.getRight() is not None:
                temp = temp.getRight()
            else:
                break
            
        if value < temp.getValue():
            temp.setLeft(newNode)
        else:
            temp.setRight(newNode)
            
    def delete(self):
        pass
        
    
    
        
    