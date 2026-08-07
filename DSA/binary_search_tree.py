class BinarySearchList:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                return self.left.add_child(data)
            else:
                return BinarySearchList(data)
        else:
            if self.left:
                return self.left.add_child(data)
            else:
                return BinarySearchList(data)

    def search_val(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search_val(val)
            else:
                False
        else:
            if self.right:
                self.left.search_val(val)
            else:
                return False
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = sel.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            min_val = self.right.delete(self)
            self.data = min_val
            self.left = self.right.delete(min_val)
        return self
        
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def find_max(self):
        if self.right is None:
            return self.data
        return self.left.find_max()

def build_trees(elements):
    print("Building element tree:", elements)
    root = BinarySearchList(elements[0]) 

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_trees(countries)
    number_trees = build_trees([17, 4, 1, 20, 9, 23, 18, 34])
    
    print("in order transvasal give this sorted_list: ", country_tree.in_order_traversal())
    print("UK is in the list? ", country_tree.search_val("UK"))
    print("Sweden is in the list? ", country_tree.search_val("Sweden"))

        
