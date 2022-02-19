
class TreeNode:
    
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None
        
    def getValue(self):
        return self.__value
    
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def setValue(self, newValue):
        self.__value = newValue
        
    def setRight(self, newRight):
        self.__right = newRight
        
    def setLeft(self, newLeft):
        self.__left = newLeft