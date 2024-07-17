
COLOR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

print("Available colors and their hex codes:")
for color, hex_code in COLOR_TO_HEX.items():
    print(f"{color:<20} : {hex_code}")
color_name = input("Enter color name: ").strip().lower()

while color_name:
    normalized_color_name = color_name.title().replace(" ", "")
    try:
        print(f"{color_name} is {COLOR_TO_HEX[normalized_color_name]}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").strip().lower()
