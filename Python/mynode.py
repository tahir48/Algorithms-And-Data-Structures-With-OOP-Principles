class Node:
    
    
    def __init__(self, value=None):
        self._value = value
        self.next = None
    
    
    @property    
    def value(self):
        return self._value
    
    
    @value.setter
    def value(self, new_value):
        self._value = new_value
    
        
    
    
class DoublyNode:
    
    
    def __init__(self, value=None):
        self._value = value
        self.next = None
        self.prev = None
    
    
    @property    
    def value(self):
        return self._value
    
    
    @value.setter
    def value(self, new_value):
        self._value = new_value
    
