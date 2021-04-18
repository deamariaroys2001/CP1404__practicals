"""
CP1404 Practical - Programming Language.
Dea Roys
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Intialise variables."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language is dynamically typed or not. """
        if self.typing == "Dynamic":
            return True

    def add_name(self, name):
        """Add name of programming language."""
        self.name = name
        return name

    def __str__(self):
        """Returns string."""
        return ("{} ,{} Typing , Reflection ={} , First appeared in {}".format(self.name, self.typing, self.reflection,                                                                               self.year))
        print(ruby.__str__())

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
languages = [ruby, python, visual_basic]

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)


