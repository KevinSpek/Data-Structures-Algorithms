

from trees.Tree import Tree
from trees.TreeNode import TreeNode

class BinaryTree(Tree):
    
    def __init__(self):
        super(BinaryTree, self).__init__()
        

    
    def insert(self, value):
        newNode = TreeNode(value)
        self._inc()
        if len(self) == 0:
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
        newNode.setParent(temp)
        
    
    def __getBiggestFromLeft(self, node):
        if node.getLeft() is None:
            return None
        temp = node.getLeft()
        while not temp.isLeaf():
            if temp.getRight() is not None:
                temp = temp.getRight()
            else:
                temp = temp.getLeft()
        return temp
    
    def __getSmallestFromRight(self, node):
        if node.getRight() is None:
            return None
        temp = node.getRight()
        while not temp.isLeaf():
            if temp.getLeft() is not None:
                temp = temp.getLeft()
            else:
                temp = temp.getRight()
        return temp
        
        
    
    def delete(self, value):
        if len(self) == 0:
            return False
        temp = self.getRoot() 
        
        while temp is not None:
            if value < temp.getValue():
                temp = temp.getLeft()
            elif value > temp.getValue():
                temp = temp.getRight()
            
            else:
                self._dec()
                if temp.isLeaf():
                    
                    if temp == self.getRoot():
                        self.setRoot(None)
                    else: 
                        temp.deleteFromParent()
                    return True
                
                if self.getRoot() == temp:
                    replacer = self.__getBiggestFromLeft(temp)
                    
                    if replacer is None:
                        self.setRoot(temp.getRight())
                    else:
                        replacer.deleteFromParent()
                        self.setRoot(replacer)
                        replacer.setRight(temp.getRight())
                        replacer.setLeft(temp.getLeft())
                    return True
                    
                        

                
                parent = temp.getParent()
                if parent.getRight == temp:
                    
                    replacer = self.__getSmallestFromRight(temp)
                    
                    if replacer is None:
                        parent.setRight(temp.getRight())
                        return True
        
                    replacer.deleteFromParent()
                    parent.setRight(replacer)
                    replacer.setRight(temp.getRight())
                    replacer.setLeft(temp.getLeft())
                    
                            
                else:
                   
                    replacer = self.__getBiggestFromLeft(temp)
                    print(replacer)
                    if replacer is None:
                        
                        parent.setLeft(temp.getRight())
                        return True
                    
                    replacer.deleteFromParent()
                    parent.setLeft(replacer)
                    replacer.setRight(temp.getRight())
                    replacer.setLeft(temp.getLeft())
                    
                return True
                    
        return False
                        
                        
                    

                    
            
            
            
                
        
        
        
        
    
    
        
    