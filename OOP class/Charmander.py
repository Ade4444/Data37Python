from pokemon import Pokemon
from move import Move

class Charmander(Pokemon):
    def __init__(self):
        super().__init__(
        name="Charmander",
        type="Fire",
        hp=7,
        attack=9,
        defence=5
    )
    self.moves.append(Move("Scratch", "Normal", 10))
    self.moves.append(Move("Growl", "Normal", 0))

char = Charmander()
print(char.type)
print(char.hp)


    class Pikachu(Pokemon):
        def __init__(self):
            super().__init__("Pikachu", "Electric",
                            hp=6, attack=6, defence=6)
        self.moves.append(Move("Thundershock", "Electric", 10))
        self.moves.append(Move("TailWhip", "Normal", 0))