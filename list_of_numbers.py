def display_menu():
    print("\nMenu:")
    print("1. Insert a number")
    print("2. Delete a number")
    print("3. Search for a number")
    print("4. Display the list")
    print("5. Exit")

def insert_number(numbers):
    try:
        num = int(input("Enter the number to insert: "))
        numbers.append(num)
        print(f"{num} inserted successfully.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_number(numbers):
    try:
        num = int(input("Enter the number to delete: "))
        if num in numbers:
            numbers.remove(num)
            print(f"{num} deleted successfully.")
        else:
            print(f"{num} not found in the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def search_number(numbers):
    try:
        num = int(input("Enter the number to search: "))
        if num in numbers:
            print(f"{num} found in the list.")
        else:
            print(f"{num} not found in the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def display_list(numbers):
    if numbers:
        print("Current list:", numbers)
    else:
        print("The list is empty.")

def main():
    numbers = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            insert_number(numbers)
        elif choice == '2':
            delete_number(numbers)
        elif choice == '3':
            search_number(numbers)
        elif choice == '4':
            display_list(numbers)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()