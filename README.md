# Library_Management_System
Library Management System (Streamlit)

A file-based Library Management System built using Python and Streamlit that allows users to manage books using full CRUD operations.
The project demonstrates file handling, validation logic, session state usage, and interactive UI development with Streamlit.

🚀 Features
 Add New Books with unique ISBN validation
 View All Books in tabular format
 Search Books by ISBN
 Update Book Details using Streamlit session state
 Delete Book Records
 Persistent storage using text file (books.txt)
 Strong input validation for ISBN, year, and empty fields

🛠️ Tech Stack
Python
Streamlit
File Handling (TXT)
OS Module

Run the Application
streamlit run app.py

🧠 How the System Works
1.Book data is stored in books.txt
2.Each record follows the format:

ISBN,Title,Author,Year,Category

3.ISBN must be numeric and unique
4.CRUD operations modify the text file dynamically
5.Streamlit session state is used to safely update records

🎯 Validation Rules
ISBN must be numeric
ISBN must be unique
Year must be 4 digits
Title, Author, and Category cannot be empty
Book must exist before update or delete

<img width="1888" height="922" alt="library" src="https://github.com/user-attachments/assets/09d11793-eabf-417d-9910-2dd43626116c" />

💡 Future Enhancements (Optional)
Replace text file with SQLite / PostgreSQL
Add search by title or author
Export books to CSV / Excel
Add user authentication
Deploy on Streamlit Cloud
