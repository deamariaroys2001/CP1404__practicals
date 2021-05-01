"""
CP1404 Practical - Guitars class .
Dea Roys
"""

CURRENT_YEAR = 2021
AGE=50
class Guitar:
    """Represent a Guitar object."""
    def __init__(self,name="", year=0,cost=0):
        """Initialise a Car instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string."""
        return "{} (): ${}".format(self.name,self.year,self.cost)

    def get_age(self):
        """return how old the guitar is in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
     """return True or False."""
     return self.get_age()>=AGE


