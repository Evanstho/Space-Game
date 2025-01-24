#Unitest for space adventure game

#what should i test???

#unit test types of ships
#Ship Damage
#Ship fighting


import Space_Adventure
import unittest

class TestPlayer(unittest.TestCase):
    """Unit tests for the player class"""

    #redo

    def test_1(self):
        """Tests to see if the player class is created correctly"""
        Space_Adventure.Player("Timmy")
        self.assertIn("Timmy", Space_Adventure.Player("Timmy").get_captain_name())
#Test creating ship classes

#Weapon class
class TestWeapon(unittest.TestCase):
    """Unit tests for the Weapon class"""

    #bad testing
    def test_1(self):
        """Tests to see if the weapon class is created correctly when called"""
        weapon = Space_Adventure.Weapons("Mass Drivers")
        self.assertIsNotNone(weapon.get_weapon_damage())
        self.assertIs(50, Space_Adventure.Weapons("Mass Drivers").get_weapon_damage())
        self.assertIs(3, Space_Adventure.Weapons("Mass Drivers").get_num_shots())
        self.assertIs("Projectile", weapon.get_weapon_type())

    def test_2(self):
        """Tests to see if #2 works"""
        weapon = Space_Adventure.Weapons("Lasers")
        self.assertIsNotNone(weapon.get_weapon_damage())
        self.assertIs(20, Space_Adventure.Weapons("Lasers").get_weapon_damage())
        self.assertIs(2, Space_Adventure.Weapons("Lasers").get_num_shots())
        self.assertIs("Beam", weapon.get_weapon_type())

class TestShip(unittest.TestCase):
    """Unit Tests for the ship class"""


#Test Boss generator

#Test Map generator



if __name__ == '__main__':
    unittest.main()




