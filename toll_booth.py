class TollBooth:
    def __init__(self):
        self.total_vehicles = 0
        self.total_toll_collected = 0.0

    def register_vehicle(self, vehicle_type):
        toll_rates = {
            "car": 2.50,
            "truck": 5.00,
            "motorcycle": 1.00
        }

        if vehicle_type in toll_rates:
            self.total_vehicles += 1
            self.total_toll_collected += toll_rates[vehicle_type]
            print(f"{vehicle_type.capitalize()} registered. Toll: ${toll_rates[vehicle_type]:.2f}")
        else:
            print("Invalid vehicle type. Please enter 'car', 'truck', or 'motorcycle'.")

    def display_summary(self):
        print("\nToll Booth Summary:")
        print(f"Total Vehicles: {self.total_vehicles}")
        print(f"Total Toll Collected: ${self.total_toll_collected:.2f}")


# Example usage
if __name__ == "__main__":
    toll_booth = TollBooth()

    while True:
        print("\nEnter vehicle type (car, truck, motorcycle) or 'exit' to quit:")
        vehicle_type = input().strip().lower()

        if vehicle_type == "exit":
            toll_booth.display_summary()
            break
        else:
            toll_booth.register_vehicle(vehicle_type)