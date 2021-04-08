"""
Dea Roys
CP1404 Practicals week 5
"""

COLORS_TO_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                  "AntiqueWhite2": "#eedfcc", "cyan3": "#00cdcd",
                  "cyan4": "#008b8b", "DarkGoldenrod": "#b8860b", "DarkGoldenrod1": "#ffb9", "blue1": "#0000ff",
                  "brown1": "#ff4040"}
print(COLORS_TO_CODE)

colour_name = input("Enter a color name from the list:")

while colour_name != "":
    if colour_name in COLORS_TO_CODE:
        print(COLORS_TO_CODE[colour_name])
    else:
        print("Enter a color name the list:")
    colour_name = input("Enter a color name from the list:")

print("Thank You")
