This is a menu-driven Python program that performs basic CRUD operations on a text file to manage employee records.
It’s built using core Python only (no external libraries, no database), making it suitable for beginners who want to understand file handling properly.

🚀 Features

Create a structured text file with headers

Insert employee records

Read/display all records

Update a specific field using Employee ID

Replace any word globally in the file

Delete a specific employee row

Delete the entire file

Simple CLI-based menu system

🧱 Data Structure

Each employee record contains:

ID

First Name

Last Name

Age

Salary

Email

Data is stored in a formatted table inside a .txt file.

Example:

 Id   FirstName       LastName        Age   Salary     Email
 1    Anas            Siddiqui        21    30000      anas@email.com

🛠️ Technologies Used

Python 3

File Handling (open, read, write, append)

OS module (for file deletion)

📂 Project Files
.
├── main.py        # Main program file
└── README.md      # Project documentation

▶️ How to Run

Clone the repository

git clone https://github.com/your-username/your-repo-name.git


Navigate to the project directory

cd your-repo-name


Run the program

python main.py

📋 Menu Options
1. Create File
2. Insert Data
3. Read File
4. Replace Data
5. Update Data
6. Delete File
7. Delete Row
8. Exit

⚠️ Known Limitations (Read This Honestly)

❌ No data validation (age/salary/email can be invalid)

❌ Not suitable for large datasets

❌ Text-file based (no database, no indexing)

❌ replace_data() may unintentionally modify headers or multiple rows

❌ No authentication or role-based access

This is not production-ready software. It’s a learning project—and that’s fine.

🎯 Learning Outcomes

By building this project, you practice:

Python file handling

String formatting and alignment

Menu-driven program design

Basic CRUD logic

Error handling using try-except

🔮 Future Improvements (If You Want to Level Up)

Switch from .txt to CSV

Add input validation

Use SQLite / MySQL

Modularize code further

Add search functionality

Convert CLI to GUI (Tkinter) or Web App (Flask)

👤 Author

Anas Siddiqui
B.Sc. Computer Science | Data Science Aspirant
