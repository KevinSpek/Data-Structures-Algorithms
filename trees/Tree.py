from abc import ABC, abstractmethod

class Tree(ABC):
    def __init__(self):
        self.__root = None
        self.__size = 0
        
    def __len__(self):
        return self.__size
    
    def getRoot(self):
        return self.__root

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
    def insert(self):
        pass
    
    @abstractmethod
    def delete(self):
        pass
            