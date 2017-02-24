import pygame


class Gamestate:
    def __init__(self):
        pass

    def init(self, gsh):
        pass

    def update(self, gsh):
        pass

    def close(self, gsh):
        pass

    @staticmethod
    def handle_events(gsh):
        other_events = []
        events = []
        if gsh.is_sleeping:
            events.append(pygame.event.wait())
        else:
            events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                gsh.close_all()
            else:
                other_events.append(event)
        return other_events
