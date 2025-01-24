# TODO: rethink this class.
# IN PROGRESS
from dataclasses import dataclass

@dataclass
class Weapons:
    """Stores ship weapon information"""
    def __init__(self, weapon):
        self._num_of_weapons = 0
        
        # TODO: setup init
        self._weapon = weapon
        self._damage = None
        self._weapon_type = None
        self._number_of_shots = None
        
        #intializes the weapons when the class is called
        for categories in self._dict_of_weapons:
            if weapon in self._dict_of_weapons[categories]:
                ship_weapon = self._dict_of_weapons[categories][weapon]
                self._damage = ship_weapon[0]
                self._number_of_shots = ship_weapon[1]
                self._weapon_type = categories

    def get_wep_name(self):
        """Returns the name of the weapon"""
        return self._weapon

    def get_weapon_damage(self):
        """Returns the damage of the weapon"""
        return self._damage

    def get_weapon_type(self):
        """Returns the weapon damage type"""
        return self._weapon_type

    def get_num_shots(self):
        """Returns the number of shots the weapon has"""
        return self._number_of_shots

    def set_damage(self):
        """Sets the damage of the weapon"""
        pass