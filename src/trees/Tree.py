from abc import ABC, abstractmethod

class Tree(ABC):
    
    def __init__(self):
        self.__root = None
        self.__size = 0
        
    def __len__(self):
        return self.__size
    
    def getRoot(self):
        return self.__root
    
    def setRoot(self, node):
        self.__root = node
        
    def _inc(self):
        self.__size += 1
    
    def _dec(self):
        if self.__size > 0:
            self.__size -= 1
            
    def preOrder(self):
        temp, res = self.__root, []
        def helper(node):
            if node is None: return
            res.append(node.getValue())
            helper(node.getLeft())
            helper(node.getRight())
        helper(temp)
        return res

        
    def inOrder(self):
        temp, res = self.__root, []
        def helper(node):
            if node is None: return
            helper(node.getLeft())
            res.append(node.getValue())
            helper(node.getRight())
        helper(temp)
        return res
            
    def postOrder(self):
        temp, res = self.__root, []
        def helper(node):
            if node is None: return
            helper(node.getLeft())
            helper(node.getRight())
            res.append(node.getValue())
        helper(temp)
        return res
    
    @abstractmethod
    def insert(self, value):
        pass
    
    @abstractmethod
    def delete(self, value) -> bool:
        pass
    
    @abstractmethod
    def find(self, value) -> bool:
        pass
            