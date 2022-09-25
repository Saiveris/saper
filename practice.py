import random


class Cell:
    def __init__(self, around_mines, mine, fl_open=True):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M      # number of mines
        self.pole = [[Cell(0, 0) for _ in range(self.N)] for _ in range(self.N)]
        self.init()

    def init(self):
        self.pole.insert(0, [Cell(0, 0) for _ in range(self.N)])  # создаем вспомогательные ряды
        self.pole.append([Cell(0, 0) for _ in range(self.N)])
        for _ in self.pole:
            _.insert(0, Cell(0, 0))
            _.append(Cell(0, 0))

        while self.M:         # задаем параметр mines для каждой клетки
            a, b = random.randint(1, self.N), random.randint(1, self.N)
            cell = self.pole[a][b]
            if not cell.mine:
                self.pole[a][b].mine = 1
                self.M -= 1

        for i in range(1, self.N + 1):  # задаем параметр around_mines для каждой клетки
            for j in range(1, self.N + 1):
                self.pole[i][j].around_mines = self.pole[i - 1][j - 1].mine + self.pole[i - 1][j].mine + \
                                               self.pole[i - 1][j + 1].mine + self.pole[i][j - 1].mine + \
                                               self.pole[i][j + 1].mine + self.pole[i + 1][j - 1].mine + \
                                               self.pole[i + 1][j].mine + self.pole[i + 1][j + 1].mine

        self.pole.pop(0)  # убираем вспомогательные клетки
        self.pole.pop()
        for _ in self.pole:
            _.pop(0)
            _.pop()

    def show(self):
        for row in self.pole:
            print(*map(lambda x: "#" if not x.fl_open else (x.around_mines if not x.mine else "*"), row))


game_pole = GamePole(10, 12)
game_pole.show()
