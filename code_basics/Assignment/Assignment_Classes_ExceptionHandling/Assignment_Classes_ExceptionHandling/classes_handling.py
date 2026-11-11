class LibraryItem:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrowed_item(self):
        if self.is_borrowed:
            raise Exception(f"the {self.title} is already borrowed")

        self.is_borrowed = True   
        return f"the {self.title} has been borroed successfully"
        
    
    def retured_item(self):
        if not self.is_borrowed:
            raise Exception(f"the {self.title} has been return")
        
        self.is_borrowed = True
        return f"the {self.title} has been teturn succesfully"


# biology = LibraryItem("NEW-SCHOOL", False)
# print(biology.borrowed_item())
# # print(biology.retured_item())

class Book(LibraryItem):
    def __init__(self, title, authour):
        super().__init__(title)
        self.authour_name = authour

# if __name__ == "__main__":
#     print(History.borrowed_item())
#     # print(History.retured_item())
#     print(History.authour_name)

class Journal(LibraryItem):
    def __init__(self, title, is_borrowed, issueNumber):
        super().__init__(title)
        self.issue_Number = issueNumber

    def category(self):
        if self.issue_Number > 0 and self.issue_Number <= 50:
            return f"{self.title} of {self.issue_Number} falls in the first category"
        elif self.issue_Number <= 100:
            return f"{self.title} of {self.issue_Number} falls in the second category"
        else:
            return f"{self.title} of {self.issue_Number} falls in the third category"


if __name__ == "__main__":
    legacy = Journal("Al-nuur", False , 123)
    History = Book("The Magic of thinking Big", "David Schewartz")
    print(History.borrowed_item())
    print(History.borrowed_item())


    
    # try:
    #     print(History.borrowed_item())
    #     print(History.borrowed_item())
    # except Exception as e:
    #     print(e)
    # print(History.retured_item())
    # print(History.authour_name)
    # print(legacy.borrowed_item())
    # print(legacy.issue_Number)
    # print(legacy.category())
#     
