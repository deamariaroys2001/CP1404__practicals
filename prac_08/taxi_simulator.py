"""
CP1404 Practical
Taxi Simulator
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive!")
    MENU = "q)uit, c)hoose taxi, d)rive"
    print(MENU)
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    choice = input(">>> ").lower()
    total_money = 0
    current_taxi = None

    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxi_list(taxis)
            taxi_number = int(input("Choose taxi:"))
            print("Bill to date: ${:.2f}".format(total_money))
            try:
                current_taxi = taxis[taxi_number]

            except IndexError:
                print("Invalid taxi choice")
                print("Bill to date: ${:.2f}".format(total_money))
            print(MENU)
            choice = input(">>> ").lower()
        elif choice == "d":
            if current_taxi == None:
                print("You need to choose a taxi before you can drive")
                print("Bill to date: ${:.2f}".format(total_money))
                print(MENU)
                choice = input(">>> ").lower()
            else:
                current_taxi.start_fare()
                distance = float(input("Drive how far?"))
                current_taxi.drive(distance)
                current_fare = current_taxi.get_fare()
                total_money += current_fare
                print("Your {} trip cost you ${}".format(current_taxi.name, current_fare))
                print("Bill to date: ${:.2f}".format(total_money))
                print(MENU)
                choice = input(">>> ").lower()
        else:
            print("Invalid Option")
            print("Bill to date: ${:.2f}".format(total_money))
            print(MENU)
            choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_money))
    print("Taxis are now:")
    display_taxi_list(taxis)

def display_taxi_list(taxis):
     i=0
     for i in range(len(taxis)):
         print("{} -{}".format(i, taxis[i]))
         i=i+1
     return

main()
