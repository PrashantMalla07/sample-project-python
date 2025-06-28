def display_books(books):
    for book in books:
        print("Book info:")
        for key, value in book.items():
            print(f"  {key}: {value}")
        print()
