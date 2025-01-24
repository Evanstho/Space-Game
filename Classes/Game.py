# Game Object
# TODO: Incomplete

class Game():
    def __init__(self):
        self._turn_list: list = []
        self._map: object = None
        self._player: object = None

    def tutorial_mode(self) -> None:
        """Space game tutorial"""
        # TODO: Tutorial
        pass

    def non_combat_mode(self, ship: object, player: object) -> None:
        """non combat"""
        print('\n')
        print('##############################################################')
        print('#########################Ship Status##########################')
        print(f'Hull: {ship._get_hull()}          Speed: {ship._get_speed()} ')
        print(f'Armor: {ship._get_armor()}         Power: {ship._get_power()}')
        print(f'Shields: {ship._get_shields()}       Fuel: {ship._get_fuel()}')
        print(f'Weapons: {ship._get_weapons()}                               ')
        print('#########################Actions##############################')
        print('             [MOVE] [CARGO] [MAP] [WEAPONS]                   ')
        print('##############################################################')
        print('\n')

        cmd = input('Please Enter a Command>  ')
        if cmd == 'move':
            # TODO:
            pass
        if cmd == 'inventory':
            # TODO:
            pass 
        if cmd == 'map':
            # TODO:
            pass
        if cmd == 'weapons':
            # TODO
            pass 

    def combat_mode(self, target1: object, target2: object) -> None:
        """combat"""
        Move_list = []

        While True:
            # TODO: Determine who goes first -- Based off speed.
            if target1._get_speed() > target2._get_speed():
                Move_list.append(target1)
                Move_list.appened(target2)
            elif target1._get_speed() < taget2._get_speed():
                Move_list.append(target2)
                Move_list.append(target1)
            else:
                # TODO: Roll dice to determine who goes first

            # TODO: Combat

            # TODO: Death Check

        pass


def _space_frontier() -> int:
    """Starts up the space frontier game mode"""
    
    # TODO: Determine S, M, L
    input("Please select a map size would you like the map? (S, M, L)>  ")

    return x, y


def game_menu() -> None:
    """Game menu"""
    print("\n")
    print("#####################################")
    print("#####################################")
    print("#        SELECT A GAME MODE         #")
    print("#####################################")
    print("#####################################")
    print("#          -Space Frontier-         #")
    print("#           -Ship Battle-           #")
    print("#            -Tutorial-             #")
    print("#####################################")
    print("\n")
    # TODO:


def tutorial() -> None:
    """Tutorial Mode"""
    # TODO: 
    pass


def game_over() -> None:
    """Game Over Screen"""
    print("#####################################")
    print("#####################################")
    print("#               GAME OVER           #")
    print("#####################################")
    print("#####################################")