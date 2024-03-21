"""
Lets try to do something cool shall we
"""
import re
def pattern_finder(file_path):
    """
    Here you will be able to find +91 Phone numbers , email address with .com in them and DOBs following the year-month-day format
    """
    with open(f"{file_path}","r+") as file:
        file_lines = file.read()
        user= int(input("What do you wanna find ?(Mobile No.- 1 Email - 2 DOB - 3): "))
        if user == 1 :
            for i in re.finditer(r"91-\d{10}",file_lines):
                yield i.group() 
        elif user == 2:
            for i in re.finditer(r"\D{1,}@\D{1,}.com",file_lines):
                yield i.group()
        elif user == 3:
            for i in re.finditer(re.compile(r"(\d{4})-(\d{2})-(\d{2})"),file_lines):
                yield i.group()
