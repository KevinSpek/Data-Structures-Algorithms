
class AVLNode(TreeNode):
    
    def __init__(self, value):
        super().__init__(value)
        self.__RightHeight = 0
        self.__LeftHeight = 0
        
    def getDiffHeight(self):
        # Positive -> right subtree is higher
        # Negative -> Left subtree is higher
        # Zero -> Balanced tree
        return self.__RightHeight - self.__LeftHeight
    
    def incRightHeight(self):
        self.__RightHeight += 1
        
    def incLeftHeight(self):
        self.__LeftHeight += 1
        
    def decRightHeight(self):
        self.__RightHeight -= 1
    
    def decLeftHeight(self):
        self.__LeftHeight -= 1
        
    
        
    