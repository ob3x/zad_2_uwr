class Board:
    def __init__(self, m, n, x, y):        
        if x <= 0 or x > m or y <= 0 or y > n:
            raise ValueError("Wartości x i y muszą być mniejsze niż wielkość planszy oraz większe od zera")
        
        self.m = m
        self.n = n
        self.x = x
        self.y = y

    def find_neighbours(self):
        points = []

        for i in range(self.x-1, self.x+2):
            for j in range(self.y-1, self.y+2):
                if i > 0 and j > 0 and i <= self.m and j <= self.n:
                    points.append((i, j))

        points.remove((self.x, self.y))
        return points

    def draw(self):
        points = self.find_neighbours()
        board = []

        for i in range(1, self.m + 1):
            line = []
            for j in range(1, self.n + 1):
                if (i, j) in points:
                    line.append("x")

                else:
                    line.append(" ")

            board.append(line)

        board[self.x - 1][self.y - 1] = "O"

        return board, points


board = Board(10, 10, 6, 3)
draw, points = board.draw()

print("")

for line in draw:
    print(line)

print(f"\n{points}\n")