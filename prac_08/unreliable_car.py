"""
CP1404 Practical
unreliable car class
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

  def __init__(self, name, fuel):
     super().__init__(name, fuel)
     self.reliability = randint(0,100)

  def drive(self,distance):
      if self.reliability > randint(0,100):
         self.distance = self.fuel
      else :
         self.distance = 0
      return self.distance

  def __str__(self):
      return "{} drives {} km. ".format(super().__str__(), self.drive(self))




