def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

if __name__ == "__main__":
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = int(input("Select an option: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print("Temperature in Fahrenheit:", fahrenheit)
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print("Temperature in Celsius:", celsius)
    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        print("Temperature in Kelvin:", kelvin)
    elif choice == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        print("Temperature in Celsius:", celsius)
    else:
        print("Invalid choice")
