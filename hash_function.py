class hashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    # def __setitem__(self, key, val):
    #     h = self.getHash(key)
    #     self.arr[h] = val

    # def __getitem__(self, key):
    #     h = self.getHash(key)
    #     return  self.arr[h]

    # def __delitem__(self, key):
    #     h = self.getHash(key)
    #     self.arr[h] = None

    # to aviod collission in the sense that when a key is alled the acess the value it will not just pick any if the random value that is inside same location but the specific value that matches the key

    def __setitem__(self, key, val):
        h = self.getHash(key)
        for i, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][i] == (key, val)
                found=True
                break
        self.arr[h].append((key,val))


    def __getitem__(self, key):
        h = self.getHash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    

    def __delitem__(self, key):
        h = self.getHash(key)
        # self.arr[h] = None
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

    def call_avg(self, key):
        sum = 0
        count = 0
        h = self.__getitem__(key)
        print(h)
        if h:
            sum += h
            count += 1
        return sum/count
        
        # return sum/len(element)



t = hashTable()

t.__setitem__("jan  1", 27)
t.__setitem__("jan  2", 31)
t.__setitem__("jan  3", 23)
t.__setitem__("jan  4", 34)
t.__setitem__("jan  5", 37)
t.call_avg("jan 1")

# t["march 5"] = 98
# t['september'] = 57
# t["march 7"] = 108
# print(t.__getitem__("september"))
# print(t.getHash("march 6"))
# print(t.arr)
# del t["march 6"]
print(t.arr)
# print(t.getHash("march 17"))
# print(t.getHash("september"))
# print(t["march 17"])
# del t["march 6"]
# print(t.__getitem__("march 5"))