FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def main():
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
    if unit == "f":
        conversion = convert_to_celsius(temperature)
        print(f"{temperature}°F is {conversion}°C")
    elif unit == "c":
        conversion = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {conversion}°F")
    else:
        print(f"Invalid temperature. Please enter a numeric value.")


def convert_to_celsius(fahrenheit):
    F_to_C = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return F_to_C

def convert_to_fahrenheit(celsius):
    C_to_F = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return C_to_F

main()
