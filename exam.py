class Book:
    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year

    def __str__(self):
        return f"'{self.title}' by {self.author}, Genre: {self.genre}, Year: {self.publication_year}"

class Library:
    instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance.books = []
        return cls._instance

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Only objects of class Book can be added")
        self.books.append(book)

    def find_book(self, title):
        found_books = [book for book in self.books if book.title == title]
        if not found_books:
            raise ValueError(f"No book found with the title '{title}'")
        return found_books

    def remove_book(self, title):
        if not any(book.title == title for book in self.books):
            raise ValueError(f"No book found with the title '{title}' to remove")
        self.books = [book for book in self.books if book.title != title]

    def books_by_genre(self, genre):
        genre_books = [book for book in self.books if book.genre == genre]
        if not genre_books:
            raise ValueError(f"No books found in the genre '{genre}'")
        return genre_books


library = Library()

try:
    book = Book("Harry Potter", "J.K. Rowling", "Fantasy", 1997)
    library.add_book(book)
    print("Book added successfully.")

    found_books = library.find_book("Harry Potter")
    for b in found_books:
        print(b)
        
    library.remove_book("The Witcher")
except ValueError as e:
    print(e)



