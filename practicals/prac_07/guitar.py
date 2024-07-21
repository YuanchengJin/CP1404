class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance. """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years."""
        CURRENT_YEAR = 2024
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Less than, used for sorting Guitars by year."""
        return self.year < other.year
