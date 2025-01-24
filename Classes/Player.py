# Description: This is the player class that keeps track of all the player info

from Classes.Dice import d6

# Race: Raccoons, Rabbits, Owl, Skunks, Mice, Foxes, Water Buffalo, Sloth,
#       Ferrets, Weasels, Badgers, Rats


class Player:
    """Keeps track of basic player information"""
    def __init__(self):
        self._player_name: str = None
        self._race: str = None
        self._hp: int = 100
        self._ship: object = None
        self._isalive: bool = True
        self._str: int = 0
        self._dex: int = 0
        self._con: int = 0
        self._int: int = 0
        self._wis: int = 0
        self._cha: int = 0
        self._statuseffects = None
        self._oxygen: int = 100
        self._level: int = 1
        self._xp: int = 0

###############################################################################
# Getters
###############################################################################
    def _get_name(self) -> str:
        """Returns the name of the captain"""
        return self._player_name

    def _get_race(self) -> str:
        """Returns the players race"""
        return self._race

    def _get_hp(self) -> int:
        """Returns the players HP"""
        return self._hp

    def _get_ship(self) -> object:
        """Returns the ship object"""
        return self.ship
        
###############################################################################
# Setters
###############################################################################
    def _set_name(self, name: str) -> None:
        """Sets the players captain name"""
        self._player_name = name

    def _set_race(self, race: str) -> None:
        """Sets the players race. Does not check paramters"""
        self._race = race

    def _set_hp(self, hp) -> None:
        """Sets the players HP"""
        self._hp = hp

    def _set_ship(self, ship: str) -> None:
        """Sets the player ship object"""
        self.ship = ship

    def _get_alivestatus(self) -> bool:
        """Returns the players status"""
        return self._isalive

    def _set_alivestatus(self) -> None:
        """Sets the alive status on the player"""
        self._isalive = not self._isalive

    def _get_str(self) -> int:
        """Returns the player strength"""
        return self._str

    def set_str(self, strength: int) -> None:
        """Sets the players strength"""
        self._str = strength

    def get_dex(self) -> int:
        """Returns the player dex"""
        return self._dex

    def set_dex(self, dexterity: int) -> int:
        """Sets the players dexerity"""
        self._dex = dexterity

    def get_con(self) -> int:
        """Returns the players constitution"""
        return self._con

    def set_con(self, constitution: int) -> int:
        """Sets the players constitution"""
        self._con = constitution

    def get_int(self) -> int:
        """Returns the player int"""
        return self._int

    def set_int(self, intelligence: int) -> int:
        """Sets the players intelligence"""
        self._int = intelligence

    def get_wis(self) -> int:
        """Returns the players wisdom"""
        return self._wis

    def set_wis(self, wisdom: int) -> int:
        """Sets the players wisdom"""
        self._wis = wisdom

    def get_cha(self) -> int:
        """Returns the players charisma"""
        return self._cha

    def set_cha(self, charisma: int) -> None:
        """Sets the players charisma"""
        self._cha = charisma

    def get_status_effect(self):
        """Returns the players status effects"""
        # TODO: Type hinting -- Array?
        return self._statuseffects

    def set_status_effects(self, effect):
        """Sets the players status effect"""
        # TODO: Type Hinting
        self._statuseffects = effect

    def get_oxygen(self) -> int:
        """Returns the players current oxygen levels"""
        return self._oxygen

    def set_oxygen(self, amount: int) -> int:
        """Sets the players current oxygen levels"""
        self._oxygen = amount

    def get_level(self) -> int:
        """Returns the players current level"""
        return self._level

    def set_level(self, level: int) -> int:
        """Sets the players level"""
        self._level = level

    def get_xp(self) -> int:
        """Returns the players current XP"""
        return self._xp

    def set_xp(self, xp: int) -> int:
        """Sets the players xp"""
        self._xp = xp

###############################################################################
# Initialize
###############################################################################
    def initialize_stats(self) -> None:
        """Function that initializes the Player stats"""
        self._str = d6(3)
        self._dex = d6(3)
        self._con = d6(3)
        self._int = d6(3)
        self._wis = d6(3)
        self._cha = d6(3)

    def initialize_name(self) -> None:
        """Initializes the Players Name"""
        name = input("What should we call you?")
        # TODO: add while loop
        self.name = name

    def initialize_race(self) -> None:
        """Initializes the players race"""
        # TODO: check the logic
        race = input('Please select from the following:' 
                     'Raccoon, Fox, Rabbit, Owl, or Skunk'
                     )
        race.lower()
        races = ['raccon', 'fox', 'rabbit', 'owl', 'skunk']
        while race not in races:
            print("Sorry that was an invalid choice")
            race = input('Please select from the following:' 
                         'Raccoon, Fox, Rabbit, Owl, or Skunk'
                         )
        self._race = race

##############################################################################
# Basic actions
###############################################################################
    def gain_experience(self, amount: int) -> None:
        """Adds experience points to the player and checks for level up"""
        self._xp += amount
        # TODO: Account for roll over
        if self._xp >= 100:
            self._level_up()

    def level_up(self) -> None:
        """Level up and boost players stats"""
        # TODO: Account for roll over
        self._level += 1
        self._xp = 0  # Sets exp back to 0
        self._str += 2
        self._dex += 2
        self._con += 2
        self._int += 1
        self._wis += 1
        self._cha += 1
        print(f"Level up! You are now level {self._level}!")

    def player_damage(self, damage: int):
        """
        Damages the player. Checks to see if the players hp is below 0
        and updates alive status.
        """
        # TODO: Apply damage to player
        # TODO: Check Hp to see if below 0 and if dead set status to None
        pass

    def oxygen_check(self):
        """
        Checks the players oxygen level and applies damage as needed
        """
        # TODO: check player oxygen level
        # TODO: if player oxygen level is below 0 then apply damage
        pass


if __name__ == '__main__':

    # Test Player stats
    print("Player Stats")

    # Initialize player test
    p = Player('Hello World')
    p.initialize_stats()

    print(f'Strength: {p.get_str()}')
    print(f'Dex: {p.get_dex()}')
    print(f'Con: {p.get_con()}')
    print(f'int: {p.get_int()}')
    print(f'Wisdom: {p.get_wis()}')
    print(f'Charisma: {p.get_cha()}')
