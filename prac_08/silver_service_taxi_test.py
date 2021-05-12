"""
CP1404 Practical
silver service taxi test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer ",200, 4)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()
