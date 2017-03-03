class Gamestate:
    """Just an abstract baseclass.

    Inherit from this baseclass. Every Gamestate should have an init, update and close method.
    The Gamestate will be managed by the Gamestatehandler class.
    """
    def __init__(self):
        """Initialize the Gamestate."""
        pass

    def init(self, gsh):
        """Initialize all attributes in the Gamestate.

        If the Gamestate is added to the Gamestatehandler queue, the method will be called once.

        Args:
            gsh: The instance of the Gamestatehandler.
        """
        pass

    def update(self, gsh):
        """Update all attributes in the Gamestate.

        Will be called every loop while the Gamestate is on top of the Gamestatehandler queue.

        Args:
            gsh: The instance of the Gamestatehandler.
        """
        pass

    def close(self, gsh):
        """Close all attributes in the Gamestate.

        This method is called if the Gamestate is removed from the Gamestatehandler queue.

        Args:
            gsh: The instance of the Gamestatehandler.
        """
        pass
