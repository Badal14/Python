def print_student(student):
    print("Name:", student['name'])
    print("Roll No:", student['roll_no'])
    print("Address:", student['address'])
    print()

def add_student(records):
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    address = input("Enter address: ")
    records[roll_no] = {'name': name, 'roll_no': roll_no, 'address': address}
    print("Student added successfully.")

def update_student(records):
    roll_no = input("Enter roll number of student to update: ")
    if roll_no in records:
        print("Current details:")
        print_student(records[roll_no])
        name = input("Enter new name (press enter to keep current): ")
        address = input("Enter new address (press enter to keep current): ")
        if name:
            records[roll_no]['name'] = name
        if address:
            records[roll_no]['address'] = address
        print("Student details updated successfully.")
    else:
        print("Student with roll number", roll_no, "not found.")

def delete_student(records):
    roll_no = input("Enter roll number of student to delete: ")
    if roll_no in records:
        del records[roll_no]
        print("Student with roll number", roll_no, "deleted successfully.")
    else:
        print("Student with roll number", roll_no, "not found.")

def main():
    student_records = {}

    while True:
        print("\n===== Student Record System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Print All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(student_records)
        elif choice == '2':
            update_student(student_records)
        elif choice == '3':
            delete_student(student_records)
        elif choice == '4':
            print("\n=== All Students ===")
            for roll_no, student in student_records.items():
                print_student(student)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
