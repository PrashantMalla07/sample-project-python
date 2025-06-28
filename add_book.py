def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    quantity = int(input("Enter quantity: "))
    book= {
        "Title": title,
        "Author": author,
        "Quantity": quantity
    }
    books.append(book)
    print("Book added successfully!")
    