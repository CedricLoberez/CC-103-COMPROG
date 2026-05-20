from datetime import datetime

books = []
members = []
loans = []


class Book:
    def __init__(self, book_id, title, author):
        self.id = book_id
        self.title = title
        self.author = author
        self.available = True


class Member:
    def __init__(self, member_id, name):
        self.id = member_id
        self.name = name


def find(data, value):
    return next((x for x in data if x.id == value), None)


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
        book = Book(
            input("Enter Book ID: "),
            input("Enter Book Title: "),
            input("Enter Book Author: ")
        )

        books.append(book)
        print("Book added:", book.title)

    elif choice == "2":
        member = Member(
            input("Enter Member ID: "),
            input("Enter Member Name: ")
        )

        members.append(member)
        print("Member registered:", member.name)

    elif choice == "3":
        book = find(books, input("Enter Book ID to borrow: "))
        member = find(members, input("Enter Member ID: "))

        if not book:
            print("Book not found.")

        elif not member:
            print("Member not found.")

        elif not book.available:
            print("Book already borrowed.")

        else:
            book.available = False

            loans.append({
                "book": book,
                "member": member,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            print(member.name, "borrowed", book.title)

    elif choice == "4":
        book_id = input("Enter Book ID to return: ")

        for loan in loans:
            if loan["book"].id == book_id:
                loan["book"].available = True
                loans.remove(loan)

                print("Book returned:", loan["book"].title)
                break

        else:
            print("Loan not found.")

    elif choice == "5":
        print("\n===== BOOK LIST =====")

        for b in books:
            print(f"{b.id} | {b.title} | {b.author} | {'Available' if b.available else 'Borrowed'}")

    elif choice == "6":
        print("\n===== MEMBER LIST =====")

        for m in members:
            print(f"{m.id} | {m.name}")

    elif choice == "7":
        print("\n===== LOAN LIST =====")

        for l in loans:
            print(f"{l['book'].title} | {l['member'].name} | {l['date']}")

    elif choice == "8":
        print("Exiting...")
        break

    else:
        print("Invalid option.")