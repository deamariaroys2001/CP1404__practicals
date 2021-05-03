"""
CP1404 Practical
GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder


__author__ = 'Dea Roys'

MILES_TO_KM = 1.60934

class Miles_To_Km(App):

    def build(self):
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def check_inputs(self):
        try:
            user_input = float(self.root.ids.input_number.text)
            return user_input
        except ValueError:
            return 0

    def handle_increment(self,value):
        """Increments the user input by 1 or -1."""
        user_input = self.check_inputs()
        incremented_value = user_input + value
        self.root.ids.input_number.text = str(incremented_value)
        self.calculation()

    def calculation(self):
        """Convert miles to km."""
        check_number = self.check_inputs()
        miles_in_km = check_number * MILES_TO_KM
        self.root.ids.output_number.text = str(miles_in_km)


Miles_To_Km().run()