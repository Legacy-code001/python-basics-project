# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next

# class Linked_List:
#     def __init__(self):
#         self.head = None

#     def insert_at_beginning(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def print(self):
#         if self.head is None:
#             print("Linked List is empty")
#             return
#         iteration = self.head
#         list_str = ""
#         while iteration:
#             list_str += str(iteration.data) + ">>"
#             iteration = iteration.next
#         print(list_str)


#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data, None)

#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)
#     def get_length(self):
#         itr = self.head
#         count = 0
#         while itr:
#             count += 1
#             itr = itr.next
#         return 
        

#     """get the value at a particular index"""
#     def get_at_index(self, index):
#         if index < 0 or index > self.get_length():
#             raise Exception("invalid index")
#             return
        
#         if index == 0:
#             self.head = self.head.next
#             return
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
#             count += 1

#     """input value at that index"""
#     def insert_at(self, index, data):
#         if index < 0 or index > self.get_length():
#             raise Exception("invalid index")
#             return
            
#         if index == 0:
#             self.insert_at_beginning(data)
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break
#             itr = itr.next
#             count += 1
    
#     # def insert_after_value(self, data_after, data_to_insert):
#     # # Search for first occurance of data_after value in linked list
#     # # Now insert data_to_insert after data_after node

#     # def remove_by_value(self, data):
#     # # Remove first node that contains data

#     def insert_after_value(self, data_after, data_to_insert):
#         current = self.head
#         while current is not None:
#             if current.data == data_after:
#                 break
#             current = current.next
#         if current is None:
#             raise Exception(f"the value '{data_after}' is not found" )
#             return
#         # create the node, 
#         new_node = Node(data_to_insert)
#         # move to the next node after it and replce it with node after 'the one' we wnt to insert after it 
#         new_node.next = current.next
#         # then we insert our new node after the 'data_after'
#         current.next = new_node

#     # Remove first node that contains data
#     def remove_by_value(self, data_to_remove):
#         if self.head == None:
#             return
#         if self.head.data == data_to_remove:
#             self.head = self.head.next
#             return
        
#         current = self.head
#         while current is not None:
#             if current.next.data == data_to_remove:
#                 current.next = current.next.next
#                 return
#             current = current.next
#         print(f"Value '{data_to_remove}' not found in the list.")
    
# class Node:
#     def __init__(self, data, next):
#         self.data
#         self.next
# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def set_beginning(self, data):
#         node = Node(data, self.head)
#         self.head = node
#     def print(self, data):
#         if self.head is None:
#             print("none")
#         itr = self.head
#         str_list = ''
#         while itr:
#             str_list += itr.data
#         itr = itr.next
#         print(str_list)

#     def put_to_end(self, data):
#         node = Node(data. None)
#         if self.head is None:
#             self.head = node
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data, None)
            
#     def addValues(self, set_values):
#         self.head = None:
#             for data in set_values:
#                 self.put_to_end(data)

#     def countLen(self):
#         if self.head is not None:
#             count = 0
#             itr = self.head
#             while itr:
#                 count+=1
#                 itr.next
#             return
        
#         def get_index(self, index):
#             if index < 0 and self.
#             itr = self.head
#             count = 0
#             while itr:
#                 itr.next
#                 count += 1
        
#         def is_match(ch1, ch2):
#             match = {
#                 "(": ")",
#                 "[": "]",
#                 "{": "}"
#             }
#             return is_match[ch1] == ch2
#         def is_balace(self, str):
#             stackedVal = stack()
#             for ch in str:
#                 if ch == "(" or ch == "[" or ch == "{":
#                     stackedVal.append(ch)
#                 if ch == ")" or ch == "]" or ch == "}":
#                     if stackedVal.len() == 0 
#                     return false
#                     if not is_matchc(ch , stackedVal.pop()):
#                         return false
#             return stackedVal.len() == 0



            



    


# if __name__ == "__main__":
#     sample_list = Linked_List("temp")
#     sample_list.insert_values([{"jan 1": 15}, {"jan 2": 35}])
#     # print("the count is", sample_list.get_length())
#     # sample_list.get_at_index(2)
#     # sample_list.insert_at(0, "agbalumo")
#     # sample_list.insert_at_end("mango")
#     # sample_list.insert_at_end("orange")
#     # sample_list.insert_after_value("pineapple", "apple")
#     # sample_list.remove_by_value("orange")
#     sample_list.print()
#     # sample_list.print_avg()

class CupNode:
    def __init__(self,data, next):
        self.data = data
        self.next = next

<<<<<<< HEAD
cupNode1 = CupNode("mueez")
print(cupNode1)
=======
<<<<<<< HEAD
cupNode1 = CupNode("mueez")
print(cupNode1)
=======
class Linked_List:
    def __init__(self, temp):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        iteration = self.head
        list_str = ""
        while iteration:
            list_str += str(iteration.data) + ">>"
            iteration = iteration.next
        print(list_str)

    # def print_avg(self):
    #     if self.head is None:
    #         print("Linked List is empty")
    #         return
    #     iteration = self.head
    #     list_str = 0
    #     while iteration:
    #         list_str += int(self.temp.data) 
    #         iteration = iteration.next
    #     print(list_str)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

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
        return 
        

    """get the value at a particular index"""
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
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next 
            count += 1

    """input value at that index"""
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

             
    
    # def insert_after_value(self, data_after, data_to_insert):
    # # Search for first occurance of data_after value in linked list
    # # Now insert data_to_insert after data_after node

    # def remove_by_value(self, data):
    # # Remove first node that contains data

    def insert_after_value(self, data_after, data_to_insert):
        current = self.head
        while current is not None:
            if current.data == data_after:
                break
            current = current.next
        if current is None:
            raise Exception(f"the value '{data_after}' is not found" )
            return
        # create the node, 
        new_node = Node(data_to_insert)
        # move to the next node after it and replce it with node after 'the one' we wnt to insert after it 
        new_node.next = current.next
        # then we insert our new node after the 'data_after'
        current.next = new_node

    # Remove first node that contains data
    def remove_by_value(self, data_to_remove):
        if self.head == None:
            return
        if self.head.data == data_to_remove:
            self.head = self.head.next
            return
        
        current = self.head
        while current is not None:
            if current.next.data == data_to_remove:
                current.next = current.next.next
                return
            current = current.next
        print(f"Value '{data_to_remove}' not found in the list.")
    



            



    def get_index(self, index):
        if index < 0  or self.len(data) > index:
            print("index is not available")
            return
        
        if index == 0:
            self.head = self.head.data
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_data_atIndex(self, index, data):
        if index < 0  or self.len(data) > index:
            print("index is not available")
            return
        node = Node(data, self.head)
        if index == 0:
            self.head = node
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = node
                break
            itr = itr.next
            count += 1
        
        def insert_data_atIndex(self, index, data):
        if index < 0  or index: > self.get_length()
            print("index is not available")
            return
        node = Node(data, self.head)
        if index == 0:
            self.head = node
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


        def insert_val(self, data_target, data_to_put):
            current = self.head
            while current is not None:
                if current == data_target:
                    break
                ccurrent = current.next

            if current is None:
                raise Exception("not value as '{data_target}' ")
                return

            node = Node(data_to_put)
            node.next = current.next
            current.next = node


        



if __name__ == "__main__":
    sample_list = Linked_List("temp")
    sample_list.insert_values([{"jan 1": 15}, {"jan 2": 35}])
    # print("the count is", sample_list.get_length())
    # sample_list.get_at_index(2)
    # sample_list.insert_at(0, "agbalumo")
    # sample_list.insert_at_end("mango")
    # sample_list.insert_at_end("orange")
    # sample_list.insert_after_value("pineapple", "apple")
    # sample_list.remove_by_value("orange")
    # sample_list.print()
    sample_list.print_avg()
>>>>>>> 33d816b (next-push)
>>>>>>> 0d57839 (first-aug)
