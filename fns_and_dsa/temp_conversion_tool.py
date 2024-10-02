# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Factor for converting Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Factor for converting Celsius to Fahrenheit
FREEZING_POINT_F = 32  # Freezing point of water in Fahrenheit

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - FREEZING_POINT_F) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_F

def main():
    while True:  # Loop for continuous user interaction
        try:
            # User input for temperature
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            
            if unit == 'F':
                celsius = convert_to_celsius(temperature)
                print(f"{temperature}°F is {celsius}°C")
            elif unit == 'C':
                fahrenheit = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {fahrenheit}°F")
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
                
            # Ask if the user wants to convert another temperature
            another_conversion = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
            if another_conversion != 'yes':
                break
            
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    print("Goodbye!")  # Exit message

if __name__ == "__main__":
    main()
