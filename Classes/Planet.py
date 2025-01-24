# Description: Planet object
# TODO: incomplete

from random import randint, choice


class Planet():
    def __init__(self):
        self._name: str = ''
        self._size: int = 0
        self._temp: int = 0
        self._race: str = None
        self._faction: str = None
        self._history: str = None
        self._shop: bool = False

###############################################################################
# Getters and Setters
###############################################################################

    def get_name(self):
        return self._name

    def get_size(self):
        return self._size

    def get_temperature(self):
        return self._temp

    def get_race(self):
        return self._race

    def get_faction(self):
        return self._faction

    def get_history(self):
        return self._history

    def has_shop(self):
        return self._shop
###############################################################################
# Basic Actions
###############################################################################

    def _generate_planet(self):
        """Initializes a Planet with random attributes"""
        self._name = self._generate_name()
        self._size = self._generate_size()
        self._temp = self._generate_temperature()
        self._race = self._generate_race()
        self._faction = self._generate_faction()
        self._history = self._generate_history()
        self._shop = self._generate_shop()

###############################################################################
    # Planet generation functions
###############################################################################
    # TODO: All these functions need to be reworked

    def _generate_name(self):
        """Generates a random name for the planet"""
        names = ["Aegon", "Vega", "Zelaris", "Xanthea", "Omicron", "Celestia"]
        return choice(names)

    def _generate_size(self):
        """Generates a random size for the planet (population/mass)"""
        return randint(100000, 1000000000)  # Population range

    def _generate_temperature(self):
        """Generates a random temperature for the planet"""
        return randint(-100, 60)  # In Celsius, could represent extreme to habitable temperatures

    def _generate_race(self):
        """Generates a random race living on the planet"""
        races = ["Human", "Zogonian", "Drakari", "Felenox", "Necrid", "Xynthian"]
        return choice(races)

    def _generate_faction(self):
        """Generates a random faction ruling the planet"""
        factions = ["The Galactic Empire", "Free Alliance", "Crimson Brotherhood", "The Covenant", "The Merchants Guild"]
        return choice(factions)

    def _generate_history(self):
        """Generates a random historical event for the planet"""
        events = [
            "A catastrophic war nearly wiped out all life on the planet.",
            "The planet was once a thriving trade hub but now lies in ruins.",
            "The planet is known for a historic discovery of an ancient alien artifact.",
            "The planet once hosted a revolutionary government that changed the galaxy.",
            "The planet was once a prison world before being liberated."
        ]
        return choice(events)

    def _generate_shop(self):
        """Randomly determines if the planet has a shop/marketplace"""
        return choice([True, False])
