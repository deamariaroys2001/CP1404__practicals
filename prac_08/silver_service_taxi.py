"""
CP1404 Practical
silver service taxi
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __int__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.fanciness * self.price_per_km

    def __str__(self):
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()

