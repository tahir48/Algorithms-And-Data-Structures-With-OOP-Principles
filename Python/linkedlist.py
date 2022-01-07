from mynode import Node


class LinkedList:

    
    def __init__(self, value):
        newnode = Node(value)
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
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    
    def pop(self):
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.tail == None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        
            
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
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
        
        
    def get(self, index):
        if index > self.length and index < 0:
            return False
        if self.length == 0:
            return
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    
        
    def remove(self, index):
        if index > self.length and index < 0:
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
            temp.next = None
        self.length -= 1
        
        
    def get_value(self, index):
        if index > self.length and index < 0:
            return False
        temp = self.get(index)
        return temp.value
    
    
    def set_value(self, index, value):
        if index > self.length and index < 0:
            return False
        if self.length == 0:
            return
        temp = self.get(index)
        temp.value = value
    
    
my_list = LinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.prepend(0)
my_list.set_value(4,400)
print('get_value method', my_list.get_value(3))
#my_list.set_value(2,300)
#print('get',my_list.get(4).value)

my_list.print_list()
#print('length',my_list.length)
