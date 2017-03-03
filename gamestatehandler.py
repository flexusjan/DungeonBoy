class Gamestatehandler:
    """A simple and fast Gamestatehandler.

        Examples:
            from gamestate import Gamestate
            from gamestatehandler import Gamestatehandler

            gsh = Gamestatehandler()
            gs = Gamestate()
            gsh.push_state(gs)

            while gsh.update()
                pass

            gsh.close()
    """

    def __init__(self):
        """Initialize the Gamestatehandler."""
        self._states = []

    def _init_state(self):
        if self._states:
            self._states[-1].init(self)

    def update_state(self):
        """Update current Gamestate.

        Calls the update method of the Gamestate on top of the queue.

        Returns: True if there are Gamestates in the queue, False if not.
        """
        if self._states:
            self._states[-1].update(self)
            return True
        else:
            return False

    def _close_state(self):
        if self._states:
            self._states[-1].close(self)

    def close(self):
        """Remove all Gamestates from queue."""
        while self._states:
            self.pop_state()

    def switch_state(self, state):
        """Remove current Gamestate from queue, adds a Gamestate to the top of the queue.

        Args:
            state: A Gamestate.
        """
        self.pop_state()
        self.push_state(state)

    def push_state(self, state):
        """Adds one Gamestate to the top of the queue.

        Args:
            state: A Gamestate.
        """
        self._states.append(state)
        self._init_state()

    def pop_state(self):
        """Remove current Gamestate from queue."""
        self._close_state()
        self._states.pop()
