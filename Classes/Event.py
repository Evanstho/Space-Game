# Description: Event object

class Events():
    def __init__(self, level):
        self._playerlevel = level
        self._event = None

    def generate_event(self):
        """Random generates an event"""
        # TODO:
        pass

    def get_event(self):
        """Returns the current event"""
        return self._event
