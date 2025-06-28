import json
import os

filename="book_library_data.json"

def load_books():
    if not os.path.exists(filename):
        return[]
    with open (filename,'r')as file:
        return json.load(file)
    

def save_books(books):
        with open(filename, 'w') as file:
            json.dump(books, file, indent=4)




















memberfile="member_library_data.json"

def load_members():
     if not os.path.exists(memberfile):
          return[]
     with open(memberfile,'r')as file:
          return json.load(file)
     
def save_members(members):
     with open(memberfile,'w')as file:
          json.dump(members,file,indent=4)
    