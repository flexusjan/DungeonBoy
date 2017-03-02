class Gamestatehandler:
    def __init__(self):
        self._states = []

    def init_state(self):
        if self._states:
            self._states[-1].init(self)

    def update_state(self):
        if self._states:
            self._states[-1].update(self)
            return True
        else:
            return False

    def close_state(self):
        if self._states:
            self._states[-1].close(self)

    def close_all(self):
        while self._states:
            self.pop_state()

    def switch_state(self, state):
        self.pop_state()
        self.push_state(state)

    def push_state(self, state):
        self._states.append(state)
        self.init_state()

    def pop_state(self):
        self.close_state()
        self._states.pop()
