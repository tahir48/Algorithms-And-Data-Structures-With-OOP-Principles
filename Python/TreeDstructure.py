from MyTreeNode import TreeNode


class BST:

    
    def __init__(self, value):
        newnode = TreeNode(value)
        self.root = newnode

        
    def insert(self, value):
        newnode = TreeNode(value)
        if self.root is None:
            self.root = newnode
            return
        temp = self.root
        while True:
            if newnode.value > temp.value:
                if temp.right is not None:
                    temp = temp.right
                else:
                    temp.right = newnode
                    return
            else:
                if temp.left is not None:
                    temp = temp.left
                else:
                    temp.left = newnode
                    return

                
    def contains(self, value):
        if self.root == None:
            return False
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            if temp.value < value:
                if temp.right is not None:
                    temp = temp.right
                else:
                    return False
            elif temp.value > value:
                if temp.left is not None:
                    temp = temp.left
                else:
                    return False
        return False
                
            
            


mytree = BST(15)
mytree.insert(12)
mytree.insert(18)
mytree.insert(17)
mytree.insert(22)
mytree.insert(14)
mytree.insert(10)
print(mytree.contains(16))
print(mytree.root.value)
print(mytree.root.left.value, mytree.root.right.value)
print(mytree.root.left.left.value, mytree.root.left.right.value,mytree.root.right.left.value,mytree.root.right.right.value)
