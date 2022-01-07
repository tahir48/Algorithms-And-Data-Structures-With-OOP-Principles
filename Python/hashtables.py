class HashTable:

    
    def __init__(self, length):
        self.length = length
        self.Table = [None] * length
        
        
    def my_hasher(self, key):
        dummy = 0
        for i in key:
            dummy = (dummy + (ord(i) * 47)) % self.length
        return dummy

    
    def print_table(self):
        for i,j in enumerate(self.Table):
            print(i,j)

            
    def set_item(self, key, value):
        index = self.myhasher(key)
        if self.Table[index] is None:
            self.Table[index] = []
        self.Table[index].append([key,value])


    def get_item(self, key):
        index = self.myhasher(key)
        if self.Table[index] is None:
            return False
        else:
            for i in range(len(self.Table[index])):
                if self.Table[index][i][0] == key:
                    return self.Table[index][i][1]



hasht = HashTable(10)
#print(hasht.myhasher('asd'))
hasht.set_item("tahir",10)
hasht.set_item("ali",48)
hasht.set_item("mehmet",23)
hasht.set_item("kemal",10)
hasht.set_item("alirza",17)
hasht.set_item("ömer",32)
hasht.print_table()
print(hasht.get_item("mehmet"))
#print(myhasher1('asdxxasd'))
