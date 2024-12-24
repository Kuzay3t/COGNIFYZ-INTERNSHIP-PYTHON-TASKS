# Temperature Converter

# This code is written for task 2 of level 1
# I am expected to create a function that converts temperatures between Celcius and Fahrenheit.

temperature = int(input("Enter temperature: "))
temperature_unit = input("Enter temperature unit (C/F): ").upper()


def temperature_converter(temperature):
    '''This code colnverts the given temperature by the user and converts it to the other temerature unit '''
    if temperature_unit == "C":
        fahrenheit_temperature =  (temperature*1.8)+32
        print(f"The converted temperature is {fahrenheit_temperature}°F")
    elif temperature_unit == "F":
        celcius_temperature = (temperature - 32) / 1.
        print(f"The converted temperature is {celcius_temperature}°C")
    else:
        return "Invalid temperature unit"

temperature_converter(temperature)

