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

    def add_organism(self) -> None:
        while True:
            x, y = self.generate_location()
            if self.is_occupied(x, y):
                self.grid[y][x] = "\033[31mO\033[0m"
                break
