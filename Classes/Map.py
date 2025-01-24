from random import randint


class Map:
    """Information about the current map"""
    def __init__(self, x, y):
        self._map = None
        self._player_location = (x, y)
        self._cur_level = 0
        self._cur_event = None
        self._map_size_x = x
        self._map_size_y = y
        # TODO: Adjust the math on Planets, po, stations
        self._planets = int(self._map_size_y * self._map_size_x / 10)
        self._poi = int(self._map_size_y * self._map_size_x / 10)
        self._stations = int(self._map_size_y * self._map_size_x / 10)

    # TODO: place player

    def _get_map(self) -> list:
        """Returns the current map object"""
        return self._map

    def _generate_map(self) -> None:
        """Generates the playable map"""
        self._map = [[' ']*self._map_size_x for i in range(self._map_size_y)]

        self._populate_map(self._planets, self._poi, self._stations)

    def _populate_map(self, planets: int, poi: int, station: int) -> None:
        """Randomly populates the map"""
        # 'P' = Player
        # '#' = space station
        # '-' = open space
        # '!' = point of interest
        # 'O' = planet
        for p in range(planets):
            randomX = randint(0, self._map_size_x - 1)
            randomY = randint(0, self._map_size_y - 1)
            print(randomY, randomX)
            self._map[randomY][randomX] = 'O'

        for i in range(poi):
            randomX = randint(0, self._map_size_x - 1)
            randomY = randint(0, self._map_size_y - 1)
            print(randomY, randomX)
            self._map[randomY][randomX] = '!'

        for s in range(station):
            randomX = randint(0, self._map_size_x - 1)
            randomY = randint(0, self._map_size_y - 1)
            print(randomY, randomX)
            self._map[randomY][randomX] = '#'

        # TODO: Astroids
        # TODO: Large black holes

    def _print_map(self) -> None:
        """Prints the map to console"""
        print('----------Star Map------------')
        for i in self._map:
            print(i)
        print('beep beep boop boop...')


if __name__ == '__main__':
    MapTest = Map(40, 150)
    MapTest._generate_map()
    MapTest._print_map()
