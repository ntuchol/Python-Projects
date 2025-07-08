import datetime

def add_entry():
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    entry = input("Enter your diary entry: ")
    with open("diary.txt", "a") as f:
        f.write(f"{date_time} - {entry}\n")
    print("Entry added successfully.")

def view_entries():
    try:
        with open("diary.txt", "r") as f:
            entries = f.readlines()
            if entries:
                for entry in entries:
                  print(entry, end="")
            else:
              print("No entries found.")
    except FileNotFoundError:
        print("No diary entries found.")

def main():
    while True:
        print("\nDiary Menu:")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()