"""
Write a Python program that converts temperatures between Fahrenheit, Celsius, and Kelvin. The program should:
Prompt the user to enter the number of temperatures they want to convert (e.g., 5).
Prompt the user to enter each temperature value and its unit (F, C, or K).
Convert all temperatures to a common unit (e.g., Celsius) and store them in a list.
Calculate the average temperature in Celsius.
Find the highest and lowest temperatures in Celsius.
Print the original temperatures with their units and their converted values with their units.

**Additional Requirements:**

- Use functions to modularize your code.
- Handle invalid units (e.g., if the user inputs something other than F, C, or K).
- Ensure that the conversion equations are correctly applied:
  - **Fahrenheit to Celsius: C = 5/9 * (F - 32)
  - **Celsius to Fahrenheit: F = 9/5 * (C + 32)
  - **Celsius to Kelvin: K = C + 273.15
  - **Kelvin to Celsius: C = K - 273.15
  - **Fahrenheit to Kelvin: K = 5/9 * (F - 32) + 273.15
  - **Kelvin to Fahrenheit: F = 9/5 * (K - 273.15) + 32
"""
def convert_temperature(temps, units, count):
    fixed_column = 2
    converted_temps = [[None for column in range(fixed_column)] for row in range(count)]
    converted_units = [[None for column in range(fixed_column)] for row in range(count)]
    for i in range(count):
        if units[i] == 'C':
            #convert Celsius to Kelvin
            kelvin = temps[i] + 273.15
            # convert Celsius to Fahrenheit
            fahrenheit = (9 / 5 * temps[i]) + 32
            converted_temps[i][0] = kelvin
            converted_units[i][0] = 'K'
            converted_temps[i][1] = fahrenheit
            converted_units[i][1] = 'F'

        elif units[i] == 'K':
            #convert Kelvin to Celsius
            celsius = temps[i] - 273.15
            # convert Kelvin to Fahrenheit
            fahrenheit = 9 / 5 * (temps[i] - 273.15) + 32
            converted_temps[i][0] = celsius
            converted_units[i][0] = 'C'
            converted_temps[i][1] = fahrenheit
            converted_units[i][1] = 'F'

        elif units[i] == 'F':
            #convert Fahrenheit to Celsius
            celsius = 5/9 * (temps[i] - 32)
            # convert Fahrenheit to Kelvin
            kelvin = 5 / 9 * (temps[i] - 32) + 273.15
            converted_temps[i][0] = celsius
            converted_units[i][0] = 'C'
            converted_temps[i][1] = kelvin
            converted_units[i][1] = 'K'

    return converted_temps, converted_units

def main():
    count = int(input("Enter the number of temperature: "))
    temps = []
    units = []

    for i in range(count):
        temp = float(input(f"Enter temperature {i + 1}: "))
        temps.append(temp)

        while True:
            unit = input("Enter the unit (°C, K, °F ): ").upper()
            if unit == 'F' or unit == 'C' or unit == 'K':
                units.append(unit)
                break
            else:
                print("Invalid input! Please enter C, K, or F.")

    converted_temperature, converted_units = convert_temperature(temps, units, count)
    print("Original Temperatures and their Conversions:\n")
    for i in range(count):
        print(f"{temps[i]:.2f} {units[i]} -> {converted_temperature[i][0]:.2f} {converted_units[i][0]} -> {converted_temperature[i][1]:.2f} {converted_units[i][1]}")

if __name__ == '__main__':
    main()


