from file_handler import load_members
from add_member import add_member
from display_member import display_members 

members = load_members()
while True:
    print("1. Add Member")
    print("2. Display Members")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_member(members)
    elif choice == '2':
        display_members(members)
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")