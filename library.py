import streamlit as st
import os

# File Storage
FILE_NAME = "books.txt"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        pass

# Helper Functions
def read_books():
    """Read all books from file and return as list of dicts."""
    books = []
    with open(FILE_NAME, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                isbn, title, author, year, category = line.split(",")
                books.append({
                    "ISBN": isbn,
                    "Title": title,
                    "Author": author,
                    "Year": year,
                    "Category": category
                })
    return books


def write_books(book_list):
    """Write full book list to file."""
    with open(FILE_NAME, "w") as f:
        for b in book_list:
            line = f"{b['ISBN']},{b['Title']},{b['Author']},{b['Year']},{b['Category']}\n"
            f.write(line)


def is_unique_isbn(isbn):
    books = read_books()
    for b in books:
        if b["ISBN"] == isbn:
            return False
    return True


def validate_fields(isbn, title, author, year, category, check_unique=True):
    """Validation rules from requirement."""
    if not isbn.isdigit():
        return "ISBN must be numeric."
    if check_unique and not is_unique_isbn(isbn):
        return "ISBN must be unique."

    if not title.strip():
        return "Title cannot be empty."
    if not author.strip():
        return "Author cannot be empty."

    if not year.isdigit() or len(year) != 4:
        return "Year must be 4 digits."

    if not category.strip():
        return "Category cannot be empty."

    return "OK"

# CRUD Operations
def add_book(isbn, title, author, year, category):
    validation = validate_fields(isbn, title, author, year, category)
    if validation != "OK":
        return validation

    books = read_books()
    books.append({
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "Year": year,
        "Category": category
    })
    write_books(books)
    return "SUCCESS"


def search_book(isbn):
    books = read_books()
    for b in books:
        if b["ISBN"] == isbn:
            return b
    return None


def update_book(isbn, title, author, year, category):
    books = read_books()
    updated = False

    for b in books:
        if b["ISBN"] == isbn:
            updated = True
            b["Title"] = title
            b["Author"] = author
            b["Year"] = year
            b["Category"] = category

    if not updated:
        return "Book not found."

    write_books(books)
    return "UPDATED"


def delete_book(isbn):
    books = read_books()
    new_books = [b for b in books if b["ISBN"] != isbn]

    if len(books) == len(new_books):
        return "Book not found."

    write_books(new_books)
    return "DELETED"

# Streamlit Interface
st.title("📚 Library Management System")

menu = ["Add New Book", "View All Books", "Search Book by ISBN", "Update Book Details", "Delete Book", "Exit"]
choice = st.sidebar.selectbox("Menu", menu)

# 1. Add New Book
if choice == "Add New Book":
    st.header("Add New Book")

    isbn = st.text_input("ISBN")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.text_input("Year")
    category = st.text_input("Category")

    if st.button("Add Book"):
        msg = add_book(isbn, title, author, year, category)
        if msg == "SUCCESS":
            st.success("Book added successfully!")
        else:
            st.error(msg)


# 2. View All Books
elif choice == "View All Books":
    st.header("All Books")

    books = read_books()
    if books:
        st.table(books)
    else:
        st.info("No books found.")

# 3. Search Book by ISBN
elif choice == "Search Book by ISBN":
    st.header("Search Book")

    isbn = st.text_input("Enter ISBN to Search")

    if st.button("Search"):
        book = search_book(isbn)
        if book:
            st.success("Book found!")
            st.json(book)
        else:
            st.error("No book found with this ISBN.")

# 4. Update Book Details (Fixed) 
elif choice == "Update Book Details":
    st.header("✏ Update Book Details")

    # STEP 1: Input ISBN
    isbn = st.text_input("Enter ISBN to Fetch Details")

    if "book_data" not in st.session_state:
        st.session_state.book_data = None

    if st.button("Fetch Book"):
        book = search_book(isbn)
        if book:
            st.session_state.book_data = book
            st.success("Book loaded! Scroll down to update.")
        else:
            st.error("Book not found.")

    # STEP 2: Show update form only if book is loaded
    if st.session_state.book_data:
        book = st.session_state.book_data

        st.subheader("Update Below")

        new_title = st.text_input("Title", book["Title"])
        new_author = st.text_input("Author", book["Author"])
        new_year = st.text_input("Year", book["Year"])
        new_category = st.text_input("Category", book["Category"])

        if st.button("Update Book Now"):
            msg = update_book(book["ISBN"], new_title, new_author, new_year, new_category)
            if msg == "UPDATED":
                st.success("Book updated successfully!")
                st.session_state.book_data = None
            else:
                st.error(msg)

# 5. Delete Book
elif choice == "Delete Book":
    st.header("Delete Book")

    isbn = st.text_input("Enter ISBN to Delete")

    if st.button("Delete"):
        msg = delete_book(isbn)
        if msg == "DELETED":
            st.success("Book deleted successfully!")
        else:
            st.error(msg)

# 6. Exit
elif choice == "Exit":
    st.info("Close the browser tab to exit the application.")

