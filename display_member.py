def display_members(members):

    for member in members:
        print("Member info:")
        for key, value in member.items():
            print(f"{key.capitalize()}:{value}")

        print()