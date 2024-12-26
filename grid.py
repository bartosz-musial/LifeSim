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

    def get_new_location(self, organism) -> tuple:
        movement = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while True:
            dx, dy = random.choice(movement)
            new_x, new_y = organism.x + dx, organism.y + dy
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                return new_x, new_y

    def update_organism_position(self, organism, new_location: tuple) -> None:
        old_x, old_y = organism.x, organism.y
        organism.move(new_location[0], new_location[1])
        self.grid[old_y][old_x] = "."
        self.grid[new_location[1]][new_location[0]] = "\033[31mO\033[0m"

    def handle_food_interaction(self, organism, new_location: tuple) -> None:
        if self.grid[new_location[1]][new_location[0]] == "\033[32mF\033[0m":
            organism.eat(10)

    def organism_movement(self, organism) -> None:
        new_location = self.get_new_location(organism)
        self.handle_food_interaction(organism, new_location)
        self.update_organism_position(organism, new_location)

    def get_vision(self, organism) -> None:
        x, y = organism.x, organism.y
        def check(dx, dy):
            if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                cell = self.grid[dy + y][dx + x]
                return "F" if cell == "\033[32mF\033[0m" else cell

        left = check(-1, 0)
        right = check(1, 0)
        up = check(0, -1)
        down = check(0, 1)

        organism.vision(left, right, up, down)
