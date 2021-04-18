"""
CP1404 Practical - Guitars class .
Dea Roys
"""

from prac_06.guitar import Guitar

guitars=[]

def main():
 print("My guitars!")
 name=input("Name:")
 while name !="":
    year = input("Year:")
    cost = input("Cost:$")
    add_guitar=Guitar(name,year,cost)
    guitars.append(add_guitar)
    print("{} ({}) : ${} added".format(name,year,cost))
    name=input("Name:")
 guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
 guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
 if guitars != []:
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
    print("Guitar {}: {} ({}), worth $ {}{}".format(i + 1, guitar.name, guitar.year,
                            guitar.cost, vintage_string))
 else :
    print("Empty List !")

main()
