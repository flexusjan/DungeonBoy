from gamestateInit import GamestateInit
from gamestatehandler import Gamestatehandler

gsh = Gamestatehandler()
gsh.push_state(GamestateInit())

while gsh.update_state():
    pass

gsh.close()
