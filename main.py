books = []
from add_book import add_book
from display_book import display_books
while True:
    print("1. Add Book")
    print("2. Display Books")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_book(books)
    elif choice == '2':
        display_books(books)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")
