from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance. """
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness

    def get_fare(self):
        """Return the price for the taxi trip, including flagfall."""
        distance_fare = super().get_fare()  # Get the fare from the parent class
        return distance_fare + self.flagfall

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, {self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}"
