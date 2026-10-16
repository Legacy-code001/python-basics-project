class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class Double_Linked_List:
    def __init__(self):
        self.head = None
        
    # insert element at the beginning 
    def insert_at_beginning(self, data):
         # 1. Create the new node pointing forward to the current head
        node = Node(data, next=self.head, prev=None)

        # 2. If the list isn't empty, point the old head backward to the new node
        if self.head is not None:
            self.head.prev = node

          # 3. CRITICAL FIXED STEP: Update the head of the list to be the new node
        self.head = node
    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        iteration = self.head
        list_str = "forward: "
        while iteration:
            list_str += str(iteration.data) + ">>"
            iteration = iteration.next
        print(list_str)

    def print_backward(self):
        if self.head is None:
            print("no element is avilable")
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        list_str = 'backard: '
        while itr:
            list_str += str(itr.data) + "...."
            itr = itr.prev
        print(list_str)

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
        node.prev = itr
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def get_at_index(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")
            return
        
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                return itr.data
            itr = itr.next
            count += 1
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")
            return
             
        if index == 0:
            self.insert_at_beginning(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    


if __name__ == "__main__":
    sample_list = Double_Linked_List()
    sample_list.insert_values(["tomato","pineapple", "date"])
    # sample_list.get_at_index(2)
    # sample_list.insert_at(0, "agbalumo")
    sample_list.insert_at_beginning("orange")
    sample_list.insert_at_beginning("mango")
    # sample_list.insert_at_beginning("plantain")
    # sample_list.insert_at_end("water mellon")
    # sample_list.insert_at_end("banana")
    sample_list.insert_at_end("cucumber")
    # sample_list.insert_at_end("water mellon")
    
    # sample_list.insert_after_value("pineapple", "apple")
    # sample_list.remove_by_value("orange")
    print(sample_list.get_at_index(2))
    sample_list.insert_at(0, "agbalumo")
    sample_list.print_forward()
    sample_list.print_backward()
    print("the count is", sample_list.get_length())