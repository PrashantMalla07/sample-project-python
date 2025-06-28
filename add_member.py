from file_handler import save_members
def add_member(members):
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    phone = input("Enter member phone number: ")
    
    member = {
        "Name": name,
        "Email": email,
        "Phone": phone
    }
    
    members.append(member)
    save_members(members)
    print("Member added successfully!")