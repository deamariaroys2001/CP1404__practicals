"""
Kivy example for CP1404
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabel(App):
    """Main program - Kivy app to demo dynamic labels creation."""


    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456",
                              "Caroline": "0421550483"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from dictionary entries and add them to the GUI."""
        for name in self.name_to_phone:
            temp_labels = Label(text=name)
            self.root.ids.main.add_widget(temp_labels)


DynamicLabel().run()
