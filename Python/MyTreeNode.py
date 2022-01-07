class TreeNode:

    
    def __init__(self, value):
        self._value = value
        self.right = None
        self.left = None
    
    
    @property
    def value(self):
        return self.value

    
    @value.setter
    def value(self, newvalue):
        self._value = newvalue

