"""Author: Desiree Blake
Purpose: Practice working with classes using OOP

"""
from turtle import title

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author.name)
        print("Year:", self.year)


""" (Notes on class breakdown) 
'Author' class represents an author and has 'name as a single attribute'
'Book' class presents a book and has attributes for 'titile', 'author', and 'year'
'Book' class has a 'display_info' method that prints all the info about the book.
"""
# Authors
author1 = Author("bell hooks")
author2 = Author("Octavia Butler")

# Books
book1 = Book("All About Love: New Visions", author1, 2000)
book2 = Book("Parable of the Sower", author2, 1993)

# Show Book Info
book1.display_info()
print()
book2.display_info()

