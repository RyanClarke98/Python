def calculate_endurance(fuel, fuel_consumption):
        # Check if fuel consumption is zero
        if fuel_consumption == 0:
            print("Error: Fuel consumption cannot be zero.")
            return 0
        return fuel / fuel_consumption

def validate_input():
    while True:
        try:
            # User input for fuel and fuel consumption
            fuel = float(input("Enter fuel in litres: "))
            fuel_consumption = float(input("Enter fuel consumption in litres per minute: "))
            
            # Calculate and print endurance
            endurance = calculate_endurance(fuel, fuel_consumption)
            if endurance > 0:
                print(f"Remaining endurance: {endurance} minutes")
                break
        except ValueError:
            print("Invalid input, please enter numeric values.")

validate_input()
