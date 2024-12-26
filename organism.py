from grid import Grid

class Organism:
    def __init__(self, x: int, y: int, energy: int):
        self.x = x
        self.y = y
        self.energy = energy

    def __str__(self):
        return f"\033[32mx: {self.x}, y: {self.y}, energy: {self.energy}\033[0m"

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.energy -= 1

    def eat(self, energy_boost: int) -> None:
        self.energy += energy_boost
