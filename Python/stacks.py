from mynode import Node

class Stack:
    
    def __init__(self,value):
        newnode = Node(value)
        self.top = newnode
        self.height = 1
    
    def print_stack(self):
        if self.top is None:
            return 
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
     
    def push(self,value):
        newnode = Node(value)
        if self.top is None:
            self.top = newnode
            return
        newnode.next = self.top
        self.top = newnode
        self.height += 1
    
    def pop(self):
        if self.height == 0:
            return
        temp = self.top.next
        self.top.next = None
        self.top = temp
        self.height -= 1
        
    
    
my_stack = Stack(0)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()


my_stack.print_stack() 
    
            
        