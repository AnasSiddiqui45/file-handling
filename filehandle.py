import os

HEADER = f"{'Id':^5} {'FirstName':^15} {'LastName':^15} {'Age':^7} {'Salary':^10} {'Email':^25}\n"

def format_row(data):
    return f"{data[0]:^5} {data[1]:^15} {data[2]:^15} {data[3]:^7} {data[4]:^10} {data[5]:^25}\n"


def create_file():
    filename = input("Enter file name: ")
    with open(filename, "w") as f:
        f.write(HEADER)
    print("File created successfully.\n")


def insert_data():
    filename = input("Enter file name: ")

    try:
        data = [
            input("ID: "),
            input("First Name: "),
            input("Last Name: "),
            input("Age: "),
            input("Salary: "),
            input("Email: ")
        ]

        with open(filename, "a") as f:
            f.write(format_row(data))
        print("Data inserted successfully.\n")

    except FileNotFoundError:
        print("File not found.\n")


def read_file():
    filename = input("Enter file name: ")
    try:
        with open(filename, "r") as f:
            print("\n" + f.read())
    except FileNotFoundError:
        print("File not found.\n")


def replace_data():
    filename = input("Enter file name: ")
    old = input("Enter word to replace: ")
    new = input("Enter new word: ")

    try:
        with open(filename, "r") as f:
            content = f.read()

        if old not in content:
            print("Word not found.\n")
            return

        with open(filename, "w") as f:
            f.write(content.replace(old, new))

        print("Data replaced successfully.\n")

    except FileNotFoundError:
        print("File not found.\n")


def update_data():
    filename = input("Enter file name: ")
    uid = input("Enter ID to update: ")

    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        with open(filename, "w") as f:
            for line in lines:
                parts = line.split()

                if parts and parts[0] == uid:
                    print("1.First Name 2.Last Name 3.Age 4.Salary 5.Email")
                    ch = int(input("Choose field: "))

                    new_value = input("Enter new value: ")
                    parts[ch] = new_value
                    f.write(format_row(parts))
                else:
                    f.write(line)

        print("Update completed.\n")

    except FileNotFoundError:
        print("File not found.\n")
    except Exception:
        print("Invalid input.\n")


def delete_row():
    filename = input("Enter file name: ")
    uid = input("Enter ID to delete: ")
    found = False

    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        with open(filename, "w") as f:
            for line in lines:
                if line.split() and line.split()[0] == uid:
                    found = True
                    continue
                f.write(line)

        print("Row deleted.\n" if found else "ID not found.\n")

    except FileNotFoundError:
        print("File not found.\n")


def delete_file():
    filename = input("Enter file name: ")
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted.\n")
    else:
        print("File not found.\n")


# ================= MAIN MENU =================

while True:
    print("""
1. Create File
2. Insert Data
3. Read File
4. Replace Data
5. Update Data
6. Delete File
7. Delete Row
8. Exit
""")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input.\n")
        continue

    if choice == 1:
        create_file()
    elif choice == 2:
        insert_data()
    elif choice == 3:
        read_file()
    elif choice == 4:
        replace_data()
    elif choice == 5:
        update_data()
    elif choice == 6:
        delete_file()
    elif choice == 7:
        delete_row()
    elif choice == 8:
        print("Exiting program.")
        break
    else:
        print("Wrong choice.\n")
