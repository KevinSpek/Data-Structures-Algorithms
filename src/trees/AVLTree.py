

from BinaryTree import BinaryTree
from nodes.AVLNode import AVLNode

class AVLTree(BinaryTree):
    
    def __init__(self):
        super(AVLTree, self).__init__()
        
        
    def fixHeight(node):
        if node.getDiffHeight() >= 2:
            pass
        elif node.getDiffHeight() <= -2:
            pass
            
        
        
        
    def insert(self, value):
        newNode = AVLNode(value)
        self._inc()
        if len(self) == 0:
            self.setRoot(newNode)
            return
        
        temp = self.getRoot()
        toFixNode = None
        while True:
            if value < temp.getValue() and temp.getLeft() is not None:
                temp.incLeftHeight()
                if abs(temp.getDiffHeight()) >= 2:
                    tofixNode = temp 
                temp = temp.getLeft()
            elif value >= temp.getValue() and temp.getRight() is not None:
                temp.incRightHeight()
                if (abs(temp.getDiffHeight())) >= 2:
                    toFixNode = temp
                temp = temp.getRight()
            else:
                break
            
        if value < temp.getValue():
            temp.setLeft(newNode)
        else:
            temp.setRight(newNode)
        newNode.setParent(temp)
    
    
    def delete(self, value):
        pass
    
   