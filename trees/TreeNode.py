
class TreeNode:
    
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None
        self.__parent = None
        
    def getValue(self):
        return self.__value
    
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right

    def getParent(self):
        return self.__parent
    
    def setValue(self, newValue):
        self.__value = newValue
        
    def setRight(self, newRight):
        self.__right = newRight
        
    def setLeft(self, newLeft):
        self.__left = newLeft
        
    def setParent(self, node):
        self.__parent = node
        
    def deleteFromParent(self):
        parent = self.__parent
        if parent is not None:
            if parent.getRight() == self:
                parent.setRight(None)
            else:
                parent.setLeft(None)
            self.setParent(None)
            
    def isLeaf(self):
        if self.__left is None and self.__right is None:
            return True
        return False