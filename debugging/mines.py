#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_victory(self):
        for y in range(self.height):
            for x in range(self.width):
                if not self.revealed[y][x] and (y * self.width + x) not in self.mines:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input(f"Enter x coordinate (0-{self.width-1}): "))
                y = int(input(f"Enter y coordinate (0-{self.height-1}): "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(f"Coordinates must be within 0-{self.width-1} and 0-{self.height-1}.")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                if self.check_victory():
                    self.print_board(reveal=True)
                    print("Congratulations! You win!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    # Customize the game parameters
    try:
        width = int(input("Enter the board width: "))
        height = int(input("Enter the board height: "))
        mines = int(input(f"Enter the number of mines (max {width * height - 1}): "))
        if mines >= width * height:
            print("Too many mines! The game will start with the default settings.")
            game = Minesweeper()
        else:
            game = Minesweeper(width, height, mines)
    except ValueError:
        print("Invalid input. Starting the game with default settings.")
        game = Minesweeper()

    game.play()