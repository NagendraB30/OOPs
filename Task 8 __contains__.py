class Library:
    def __init__(self):
        self.books = ["Python", "Java", "C++"]

    def __contains__(self, item):
        return item in self.books

lib = Library()

print("Python" in lib)  
print("Ruby" in lib)    