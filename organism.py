from q_learning import Q

class Organism:
    def __init__(self, x: int, y: int, energy: int):
        self.x = x
        self.y = y
        self.energy = energy
        self.age = 0
        self.vision_list = []

    def __str__(self):
        return f"\033[32mx: {self.x}, y: {self.y}, energy: {self.energy}, age: {self.age}\nvision: {self.vision_list}\033[0m"

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.energy -= 1
        self.age += 1

    def eat(self, energy_boost: int) -> None:
        self.energy += energy_boost

    def vision(self, left: int, right: int, up: int, down: int) -> None:
        self.vision_list = [left, right, up, down]
        state = (self.x, self.y, tuple(self.vision_list))
        if state not in Q:
            Q[state] = {action: 0 for action in ['left', 'right', 'up', 'down']}
