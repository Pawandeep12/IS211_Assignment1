class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    def display(self):
        print(f"{self.title}, written by {self.author}")
# Creating the first book object
book1 = Book(author="J.K. Rowling", title="Harry Potter and the Goblet of Fire")

# Creating the second book object
book2 = Book(author="Walter Scott", title="Ivanhoe: A Romance")

# Display the details of both books
book1.display()
book2.display()
