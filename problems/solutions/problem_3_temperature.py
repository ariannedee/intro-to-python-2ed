"""
Convert a temperature from Fahrenheit to Celsius
"""
temp_f = float(input("Temp in °F: "))

temp_c = (temp_f - 32) * 5 / 9

print("Temp in °C: " + str(round(temp_c, 1)))
