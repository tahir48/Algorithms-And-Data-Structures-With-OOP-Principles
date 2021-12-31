from typing import NewType
from mynode import Node


class Queue:
    
    def __init__(self,value):
        newnode = Node(value)
        self.front = newnode
        self.rear = newnode
        self.length = 1
        
    def print_queue(self):
        if self.front is None:
            return 
        temp = self.front
        while temp is not None:
            print(temp.value)
            temp = temp.next 
    
    def enqueue(self,value):
        newnode = Node(value)
        if self.length == 0:
            self.rear = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode   
        self.length += 1
        
            
    
    def dequeue(self):
        if self.length == 0:
            return
        temp = self.front
        if self.length == 1:
            self.rear = None
            self.front = None
        else:
            self.front = self.front.next
            temp.next = None
        self.length -= 1
        
        
    
    
myqueue = Queue(0)
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
#myqueue.dequeue()


#myqueue.dequeue()
myqueue.print_queue()
