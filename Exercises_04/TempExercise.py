kelvin_temps = [290.15, 295.15, 300.15, 305.15, 310.15, 315.15, 320.15, 325.15, 330.15, 335.15]

for kelvin in kelvin_temps:
    cel = kelvin - 273.15
    far = (kelvin - 273.15) * 9/5 + 32
    print(f"kelvin:{kelvin:} K | Celsius:{cel:} Celsius | Fahrenheit:{far:} Fahrenheit")
