from mynode import DoublyNode


class DoublyLinkedList:
    
    def __init__(self, value):
        newnode = DoublyNode(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1
        
        
    def print_list(self):
        if self.head == None:
            return 
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = DoublyNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    
    def pop(self):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.tail == None
        else:
            temp = self.tail.prev
            temp.next = None
            self.tail = temp
        self.length -= 1
        
            
    
    
    def prepend(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
    
    
    
    def pop_first(self):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
        self.length -= 1
        
        
    def get(self,index):
        if index > self.length or index < 0:
            return False
        if self.length == 0:
            return
        temp = self.head 
        if index < self.length/2: 
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length-1 ,index,-1):
                temp = temp.prev
        return temp
        
    
    def remove(self, index):
        if index > self.length or index < 0:
            return False
        if self.length == 0:
            return
        if index == 0:
            self.pop_first()
        elif index == self.length:
            self.pop()
        else:  
            before = self.get(index-1)
            temp = before.next
            before.next = temp.next
            temp.next.prev = before
            temp.next = None
            temp.prev = None
        self.length -= 1
        
        
    def get_value(self, index):
        if index > self.length or index < 0:
            return False
        temp = self.get(index)
        return temp.value
    
    def set_value(self, index, value):
        if index > self.length or index < 0:
            return False
        if self.length == 0:
            return
        temp = self.get(index)
        temp.value = value
    
    
    
    
my_dlist = DoublyLinkedList(1)
my_dlist.append(2)
my_dlist.append(3)
my_dlist.append(4)
my_dlist.prepend(0)
my_dlist.append(5)
my_dlist.append(6)
my_dlist.append(7)
#my_dlist.pop_first()
#print('get',my_dlist.get(7))
#print('get_value',my_dlist.get_value(8))
my_dlist.set_value(8,400)
#my_dlist.pop()


my_dlist.print_list()
