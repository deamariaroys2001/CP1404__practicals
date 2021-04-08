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
        print("Invalid entry ")
    colour_name = input("Enter a color name from the list:")

print("Thank You")

# """
# Lee Crawford
# CP1404/CP5632 Practical
# hex_colours
# """

# HEX_COLOURS = {"aquamarine1": "#7fffd4", "black": "#000000", "BlanchedAlmond": "#ffebcd",
#                "BlueViolet": "#8a2be2", "burlywood3": "	#cdaa7d", "CadetBlue2": "#8ee5ee",
#                "chartreuse2": "#76ee00", "chocolate1": "#ff7f24", "DarkGoldenrod1": "#ffb90f",
#                "DarkOliveGreen4": "#6e8b3d"}
#
# empty_value = True
#
# colour_name = input("Enter colour name: ").lower()
# while empty_value:
#     colour_hash = [hex_number for key, hex_number in HEX_COLOURS.items() if colour_name in key.lower()]
#     if not colour_hash:  # check its not empty
#         print("Please enter a valid colour")
#         colour_name = input("Enter colour name: ").lower()
#     else:
#         empty_value = False
# print(colour_hash)