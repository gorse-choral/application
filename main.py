# main.py
from book import Book
from library import Library

def get_numeric_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_library(library):
    print("\nLibrary:")
    books = library.get_books()
    if not books:
        print("No books in the library.")
    else:
        for book in books:
            print(f"{book.title} by {book.author}")

def main():
    library = Library()

    while True:
        print("\nMenu:\n1. Add Book\n2. View Library\n3. Exit")
        choice = get_numeric_input("Enter your choice: ")

        if choice == 1:
            book_title = input("Enter book title: ")
            book_author = input("Enter book author: ")
            new_book = Book(book_title, book_author)
            library.add_book(new_book)
            print("Book added to library.")
        elif choice == 2:
            display_library(library)
        elif choice == 3:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
