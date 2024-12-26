import random

class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [["." for _ in range(width)] for _ in range(height)]

    def print_grid(self) -> None:
        for line in self.grid:
            for cell in line:
                print(cell, end=" ")
            print()

    def generate_location(self) -> tuple:
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def is_occupied(self, x: int, y: int) -> bool:
        return self.grid[y][x] == "."

    def add_food(self) -> None:
        while True:
            x, y = self.generate_location()
            if self.is_occupied(x, y):
                self.grid[y][x] = "\033[32mF\033[0m"
                break

    def add_organism(self) -> tuple:
        while True:
            x, y = self.generate_location()
            if self.is_occupied(x, y):
                self.grid[y][x] = "\033[31mO\033[0m"
                return x, y

    def organism_movement(self, organism) -> None:
        movement = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while True:
            dx, dy = random.choice(movement)
            location = [organism.x, organism.y]
            temp = [organism.x, organism.y]
            temp[0] += dx
            temp[1] += dy
            if temp[0] > 0 and temp[1] > 0:
                organism.x, organism.y = temp[0], temp[1]
                organism.energy -= 1
                self.grid[location[1]][location[0]] = "."
                self.grid[temp[1]][temp[0]] = "\033[31mO\033[0m"
                break
