from datetime import datetime

books = []
members = []
loans = []


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


class Loan:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.date_borrowed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")

    book = Book(book_id, title, author)
    books.append(book)

    print(f"Book added: {title}")


def register_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")

    member = Member(member_id, name)
    members.append(member)

    print(f"Member registered: {name}")


def borrow_book():
    book_id = input("Enter Book ID to borrow: ")
    member_id = input("Enter Member ID: ")

    book = next((b for b in books if b.book_id == book_id), None)
    member = next((m for m in members if m.member_id == member_id), None)

    if not book:
        print("Book not found.")
        return

    if not member:
        print("Member not found.")
        return

    if not book.available:
        print("Book is already borrowed.")
        return

    loan = Loan(book, member)
    loans.append(loan)
    book.available = False

    print(f"{member.name} borrowed '{book.title}'")


def return_book():
    book_id = input("Enter Book ID to return: ")

    for loan in loans:
        if loan.book.book_id == book_id:
            loan.book.available = True
            loans.remove(loan)

            print(f"Book returned: {loan.book.title}")
            return

    print("Loan record not found.")


def view_books():
    if not books:
        print("No books available.")
        return

    print("\n===== BOOK LIST =====")

    for book in books:
        status = "Available" if book.available else "Borrowed"

        print(f"""
Book ID : {book.book_id}
Title   : {book.title}
Author  : {book.author}
Status  : {status}
""")


def view_members():
    if not members:
        print("No members registered.")
        return

    print("\n===== MEMBER LIST =====")

    for member in members:
        print(f"""
Member ID : {member.member_id}
Name      : {member.name}
""")


def view_loans():
    if not loans:
        print("No active loans.")
        return

    print("\n===== LOAN LIST =====")

    for loan in loans:
        print(f"""
Book     : {loan.book.title}
Borrower : {loan.member.name}
Date     : {loan.date_borrowed}
""")


while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        register_member()

    elif choice == "3":
        borrow_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        view_books()

    elif choice == "6":
        view_members()

    elif choice == "7":
        view_loans()

    elif choice == "8":
        print("Exiting program...")
        break

    else:
        print("Invalid option.")