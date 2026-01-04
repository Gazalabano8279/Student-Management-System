students = {}
def add_student():
    reg_no = int(input("Enter reg number: "))
    if reg_no in students:
        print("Student already exists!")
    else:
        name = input("Enter Name: ")
        dept = input("Enter Department: ")
        marks = int(input("Enter Marks"))
        
        students[reg_no] = {
            "name": name,
            "department": dept,
            "marks": marks
        }
        print("Student added successfully")
        
def view_students():
    if not students:
        print("No student records found.")
    else:
        for reg_no, details in students.items():
            print("Reg:",reg_no)
            print("Name:", details["name"] )
            print("Department:",details["department"])
            print("Marks:",details["marks"] )
            print("----------")
        
def search_student():
    reg_no = int(input("Enter reg number to search: "))
    if reg_no in students:
        details = students[reg_no]
        print("Student found")
        print("Name:", details["name"])
        print("Department:", details["department"])
        print("Marks:", details["marks"])
    else:
        print("Student not found")           
while True:
    print("\n-------Student Management System-------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting Program..")
    else:
        print("Invalid Choice")

