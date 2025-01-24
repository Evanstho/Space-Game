# Description: Ship class that keeps track of all the ship information

# IN PROGRESS
from Classes.Dice import d20


class Ship:
    """
    Initializes a new ship object with deserialized data from a json file.
    Stores important ship information
    """
    def __init__(self, Class, Sub, Max_Weapons, Weapons,
                 Sheilds, Armor, Hull, Speed, Power, Max_Cargo, Fuel, Layout):

        # Ship status attributes
        self._ship_name: str = None
        self._engine_on: bool = False
        self._isalive: bool = True

        # Ship type
        self._class: str = Class
        self._sub: str = Sub

        # Ship status
        self._max_weapons: int = Max_Weapons
        self._weapons: list = Weapons                                           # array of weapons cannot exceed self._max Weapons
        self._shields: int = Sheilds
        self._armor: int = Armor
        self._hull: int = Hull
        self._speed: int = Speed    # "Defense is based on speed"
        self._power: int = Power
        self._max_cargo: int = Max_Cargo
        self._cargo: list = []
        self._fuel: int = Fuel

        # Unused Attributes
        self._crew_num: int = 0
        self._status_effects: list = []
        self._layout: list = Layout
        self._oxygenlevel: int = 100

    def __repr__(self):
        return (f'Name: {self._ship_name}, '
                f'Engine: {self._engine_on}, '
                f'Alive: {self._isalive}, '
                f'Class: {self._class}, '
                f'Sub: {self._sub}, '
                f'Max Weapons: {self._max_weapons}, '
                f'Weapons: {self._weapons}, '
                f'Shields: {self._shields}, '
                f'Armor: {self._armor}, '
                f'Hull: {self._hull}, '
                f'Speed: {self._speed}, '
                f'Power: {self._power}, '
                f'Max Cargo: {self._max_cargo}, '
                f'Cargo: {self._cargo}, '
                f'Fuel: {self._fuel}, '
                )

###############################################################################
# Getters
###############################################################################
    def _get_ship_name(self) -> str:
        """Returns the name of the ship"""
        return self._ship_name

    def _get_engine(self) -> str:
        """Returns the engine status of the ship"""
        return self._engine_on

    def _get_isalive(self) -> str:
        """Returns the alive status of the ship"""
        return self._isalive    

    def _get_class(self) -> str:
        """Returns the ship's class"""
        return self._ship_class

    def _get_sub_class(self) -> str:
        """Returns the ship's sub class"""
        return self._ship_sub_class

    def _get_max_weapons(self) -> int:
        """Returns the maximum number of weapons the ship can have"""
        return self._max_weapons

    def _get_weapons(self) -> list:
        """Returns the array of weapons the ship has equiped"""
        return self._weapons

    def _get_shields(self) -> int:
        """Returns the ships shields"""
        return self._shields

    def _get_armor(self) -> int:
        """Returns the ships maximum armor"""
        return self._armor

    def _get_hull(self) -> int:
        """Returns the ships hull"""
        return self._hull

    def _get_speed(self) -> int:
        """Returns the ships speed"""
        return self._speed

    # def get_ship_max_crew(self) -> int:
    #     """Returns the ships max crew"""
    #     return self._max_crew

    def _get_power(self) -> int:
        """Returns the ships power"""
        return self._power

    def _get_max_cargo(self) -> int:
        """Returns the ships max cargo"""
        return self._max_cargo

    def _get_cargo(self) -> list:
        """Returns the list of items the ship has in the cargo"""
        return self._cargo

    def _get_fuel(self) -> int:
        """Returns the ships fuel"""
        return self._fuel

    def _get_status_effects(self) -> list:
        """
        Returns the array of the status effects currently effecting the ship
        """
        return self._status_effects

    def _get_layout(self) -> list:
        """Returns the ships layout"""
        return self._ship_layout

    def _get_oxygenlevel(self) -> int:
        """Returns the ships oxygenlevel"""
        return self._oxygenlevel

###############################################################################
# Setters
###############################################################################
    def _set_name(self, name: str) -> None:
        """Sets the name of the ship"""
        self._ship_name = name

    def _set_engine_on(self) -> None:
        """Turns the engine on and off"""
        self._engine_on = not self._engine_on

    def _set_isalive(self) -> None:
        """Sets isalive status"""
        self._isalive = not self._isalive

    def _set_weapons(self, arr: list) -> None:
        """Sets the ships weapons to an array"""
        self._weapons = arr

    def _set_shield(self, shields: int) -> None:
        """Sets the shields to variable"""
        self._shields = shields

    def _set_armor(self, armor: int) -> None:
        """Sets the armor of a ship"""
        self._armor = armor

    def _set_hull(self, hull: int) -> None:
        """Sets the hull of a ship"""
        self._hull = hull

    def _set_speed(self, speed: int) -> None:
        """Sets the speed of the ship"""
        self._speed = speed

    def _set_power(self, power: int) -> None:
        """Sets the powerlevel of the ship"""
        self._powerlevel = power

    def _set_cargo(self, cargo: list) -> None:
        """Sets the new cargo for the ship"""
        self._cargo = cargo

    def _set_fuel(self, amt: int) -> None:
        """Sets the fuel for the ship"""
        self._fuel = amt

    def _set_crew(self, num: int) -> None:
        """Sets the number of crew members on the ship"""
        self._crew_num = num

    def _set_status_effects(self, effects: list) -> None:
        """Sets the status effects of the ship"""
        self._status_effects = effects

    def _set_layout(self, arr: list) -> None:
        """Sets the ships layout"""
        self._layout = arr

    def _get_powerlevel(self):
        """Returns the powerlevel of the ship"""
        return self._powerlevel

    def _set_oxygenlevel(self, oxygen: int) -> None:
        """Sets the oxygen level on the ship"""
        self.get_oxygenlevel = oxygen

###############################################################################
# initialize Ship
###############################################################################
    def _initialize(self) -> None:
        """Initilizes the ship"""
        name = input('Looks like this is a new ship.'
                     'What should we name the ship?: ')
        verify = input("Are you sure? (y/n): ")
        verify.lower()
        while verify != 'y':
            name = input('Please enter a new name: ')
            verify = input('Are you sure? (y/n): ')
        self._ship_name = name

###############################################################################
# Basic Actions
###############################################################################
    # Needs Testing
    def _add_weapons(self, weapon: object) -> bool:
        """
        Add weapons to the array of weapons.
        Checks to see if the maximum number of weapons has been reached.
        Returns True if weapon is successfully added
        """
        # Check self._weapons to self._max_weapons
        if len(self._weapons) == self._max_weapons:
            print('Sorry you already have the maximuim number of weapons '
                  'Please remove a waepon and try again.'
                  )
            return False
        self._weapons.append(weapon)
        return True

    def _remove_weapon(self, weapon: str) -> bool:
        """
        Remove weapon from the ship
        """
        if weapon in self._weapons:
            self._weapons.pop(weapon)
            return True
        return False

    def _move(self, map: object, move: int) -> bool:
        """
        Moves the ship to the specified grid square.
        Checks how much fuel the ship has prior to moving.
        """
        if self._fuel > 2:
            
        # TODO: Check if valid move
        # TODO: Make move
        # TODO: updates player location on the map
            pass

    def _attack(self, target: object) -> bool:
        """
        Attacks the target
        """
        # TODO: Consider costing energy
        if d20(1) > target.get_speed():
            return True
        return False

    def _dodge(self) -> bool:
        """Consumes power to dodge an attack"""
        # TODO:
        return False

    def _flee(self) -> bool:
        """
        Attempt to flee
        Rolls 2 D20.
        Returns True if the ship successfully flees else returns False
        Costs Fuel to flee
        """
        player = d20(1)
        enemy = d20(1)
        if player > enemy and self._ship.fuel > 5:
            return True
        return False

    def _fire_weapon(self, weapon: object, target: object) -> None:
        """
        Fires the ships weapon
        Helper function for _attack
        """
        for i, w in enumerate(self._weapons):
            pass
            # weapon.get_damage()
            # Call object that is being shot at and apply the damage to that ship
                 
    def _deploy_drones(self) -> bool:
        """
        Checks to see if a ship has drones in their cargo
        and if so, deploys them.
        """
        # TODO:
        pass

    def _boarding(self, ship, target):
        """Starts the ships boarding process."""
        # TODO:
        pass



###############################################################################
# Recharge functions
###############################################################################

    def _recharge_sheilds(self) -> None:
        """Recharges the ships shields"""
        self._shields += 5

    def _recharge_power(self) -> None:
        """Recharges the ships power"""
        self._power += 10

    def _recharge_fuel(self, amt) -> None:
        """Adds fuel"""
        self._fuel += amt

###############################################################################
# Apply Effects
###############################################################################
    def _take_damage(self, damage) -> None:
        """Applies Damage the to ship"""
        # TODO:
        pass

    def _blast_doors(self):
        """Opens and closes all blast doors."""
        # TODO:
        pass


###############################################################################
    # REDESIGN#
###############################################################################

#     def fire_weapons(self, target):
#         """Fires the ships weapons"""
#         dice = Dice()
#         attacker = self.get_type()
#         reciever = target.get_type()
#         for wep in self.get_weapon():
#             num_shots = wep.get_num_shots()
#             print(f"############### {attacker} Fired the {wep.get_wep_name()}! ###############")
#             while num_shots > 0:
#                 ship_dice = dice.d20() + random.randint(1, self.get_speed())
#                 target_dice = dice.d20() + random.randint(1, target.get_speed())

#                 num_shots -= 1
#                 shield_damage = 0
#                 armor_damage = 0
#                 hull_damage = 0
#                 if ship_dice > target_dice:
#                     print(f"ship_dice:{ship_dice} target_dice: {target_dice}")
#                     print(f" shields:{target.get_shield()} armor: {target.get_armor()} hull: {target.get_hull()}")
# #accounts for missiles - not currently implemented
#                     # if wep.get_weapon_type() == "Projectile":
#                     #     if target.get_armor() > 0:
#                     #         armor_damage = target.get_armor() - wep.get_weapon_damage()
#                     #         if armor_damage < 0:
#                     #             target.set_armor(0)
#                     #             print(f"Ouch Captain we cracked their armor! Damaging their HULL for {hull_damage}!")
#                     #             hull_damage = abs(armor_damage)
#                     #     else:
#                     #         hull_damage = target.get_hull() - wep.get_weapon_damage()
#                     #         target.set_hull(hull_damage)
# #Accounts for ion lasers -- not currently implemented
#                     #if wep.get_weapon_type() == "Plasma":

#                     if target.get_shield() > 0:
#                         shield_damage = target.get_shield() - wep.get_weapon_damage()
#                         #Currently -- no spill over...absorbs all the damage when it breaks
#                         if shield_damage < 0:
#                             target.set_shield(0)
#                             print(f"{attacker} broke {reciever} SHIELDS!")
#                         else:
#                             target.set_shield(shield_damage)
#                             print(f"{attacker} hit {reciever} SHIELDS for {wep.get_weapon_damage()}!")
#                     elif target.get_armor() > 0:
#                         armor_damage = target.get_armor() - wep.get_weapon_damage()
#                         if armor_damage < 0:
#                             target.set_armor(0)
#                             print(f"{attacker} busted {reciever} ARMOR!")
#                         else:
#                             target.set_armor(armor_damage)
#                             print(f"{attacker} hit {reciever} ARMOR for {wep.get_weapon_damage()}!")
#                     else:
#                         hull_damage = target.get_hull() - wep.get_weapon_damage()
#                         target.set_hull(hull_damage)
#                         print(f"{attacker} damaged {reciever} Hull for {wep.get_weapon_damage()}!")
#                         #Death check
#                         # if hull_damage < 0:
#                         #     target.set_hull(0)
#                         #     print(f"Captain We've Blown them Up!")
#                 else:
#                     print(f"{attacker} missed {reciever}")

#                 # Put a death check right here
#                 target.death_check()
