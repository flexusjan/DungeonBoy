class Gamestatehandler:
    def __init__(self):
        self.states = []
        self.events = []
        self.is_sleeping = False

    def init_state(self):
        if len(self.states) > 0:
            self.states[-1].init(self)

    def update_state(self):
        if len(self.states) > 0:
            self.events = self.states[-1].handle_events(self)
        else:
            return False

        if len(self.states) > 0:
            if not self.is_sleeping:
                self.states[-1].update(self)
        else:
            return False

        return True

    def close_state(self):
        if len(self.states) > 0:
            self.states[-1].close(self)

    def close_all(self):
        while self.states:
            self.pop_state()

    def switch_state(self, state):
        self.pop_state()
        self.push_state(state)

    def push_state(self, state):
        self.states.append(state)
        self.init_state()

    def pop_state(self):
        self.close_state()
        self.states.pop()
