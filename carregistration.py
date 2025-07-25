
car_registry = {}

def add_car(plate_number, owner_name):
    if plate_number in car_registry:
        print(f"Plate number {plate_number} is already registered.")
    else:
        car_registry[plate_number] = owner_name
        print(f"Car with plate number {plate_number} registered successfully.")

def view_cars():
    if not car_registry:
        print("No cars registered yet.")
    else:
        print("Registered Cars:")
        for plate, owner in car_registry.items():
            print(f"Plate: {plate}, Owner: {owner}")

def remove_car(plate_number):
    if plate_number in car_registry:
        del car_registry[plate_number]
        print(f"Car with plate number {plate_number} removed successfully.")
    else:
        print(f"No car found with plate number {plate_number}.")

while True:
    print("\nCar Registration System")
    print("1. Add Car")
    print("2. View Cars")
    print("3. Remove Car")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        plate = input("Enter plate number: ")
        owner = input("Enter owner's name: ")
        add_car(plate, owner)
    elif choice == "2":
        view_cars()
    elif choice == "3":
        plate = input("Enter plate number to remove: ")
        remove_car(plate)
    elif choice == "4":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
