
class Node:
    def __init__(self, value) -> None:
        self.__next = None
        self.__value = value
        self.__parant = None
    
    def getNext(self):
        return self.__next

    def getValue(self):
        return self.__value
    
    def getParent(self):
        return self.__parant
    
    def setParent(self, newParent):
        self.__parant = newParent
    
    def setNext(self, newNext):
        self.__next = newNext
    
    def setValue(self, newValue):
        self.__value = newValue