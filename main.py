from gamestateInit import GamestateInit
from gamestatehandler import Gamestatehandler


def main():
    gsh = Gamestatehandler()
    gsh.push_state(GamestateInit())

    while gsh.update_state():
        pass

    gsh.close_all()


if __name__ == '__main__':
    main()
