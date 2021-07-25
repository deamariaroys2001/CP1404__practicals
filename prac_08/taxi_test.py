"""
CP1404 Practical
Taxi Test
"""
from prac_08.taxi import Taxi


def main():
    """Demo test code to show how to use taxi class."""
    taxi = Taxi("Prius 1",100)
    taxi.drive(40)
    print("{}, {}, ${}/km".format(taxi.name,taxi.fuel, taxi.price_per_km))

    taxi.start_fare()
    taxi.drive(100)
    print("{}, {}, ${}/km".format(taxi.name,taxi.fuel, taxi.price_per_km))

main()







