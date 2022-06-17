class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

     def search(self, find_data):
         if self.data == find_data:
             return self
         elif find_data < self.data and self.left != None:
             return self.left.search(find_data)
         elif find_data > self.data and self.right != None:
             return self.right.search(find_data)
         else:
            return None
