"""
CP1404 Practical - Guitars class .
Dea Roys
"""

from prac_06.guitar import Guitar

def main():
 """test guitar object."""
 guitar = Guitar("Guitar",1922,16035.40)
 another_guitar = Guitar("Another_Guitar",2013,1000)

 print("{} get_age()- Expected {}. Got {}".format(guitar.name,99,
                                                  guitar.get_age()))
 print("{} get_age()- Expected {}. Got {}".format(another_guitar.name, 8,
                                                  guitar.get_age()))

 print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True,
                                                  guitar.is_vintage()))
 print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name,False,
                                                  guitar.is_vintage()))

main()


