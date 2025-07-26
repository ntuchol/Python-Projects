def display_menu():
    print("\nPhone Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact(phone_book):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    phone_book[name] = {"Phone": phone, "Email": email}
    print(f"Contact '{name}' added successfully!")

def view_contacts(phone_book):
    if not phone_book:
        print("Phone book is empty.")
    else:
        print("\nContacts:")
        for name, details in phone_book.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")

def search_contact(phone_book):
    name = input("Enter the name to search: ").strip()
    if name in phone_book:
        details = phone_book[name]
        print(f"Found Contact - Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")
    else:
        print(f"No contact found with the name '{name}'.")

def delete_contact(phone_book):
    name = input("Enter the name to delete: ").strip()
    if name in phone_book:
        del phone_book[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    phone_book = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_contact(phone_book)
        elif choice == "2":
            view_contacts(phone_book)
        elif choice == "3":
            search_contact(phone_book)
        elif choice == "4":
            delete_contact(phone_book)
        elif choice == "5":
            print("Exiting Phone Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
