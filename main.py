class Board:
    def __init__(self, m : int, n : int, x : int, y : int) -> None:        
        if x <= 0 or x > m or y <= 0 or y > n:
            raise ValueError("Współrzędne muszą mieścić się w granicach planszy.")
        
        self.m = m
        self.n = n
        self.x = x
        self.y = y

    def find_neighbours(self) -> list:
        points = []

        for i in range(self.x-1, self.x+2):
            for j in range(self.y-1, self.y+2):
                if i > 0 and j > 0 and i <= self.m and j <= self.n:
                    points.append((i, j))

        points.remove((self.x, self.y))
        return points

    def draw(self) -> list:
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

    def print(self) -> None:
        draw, points = self.draw()

        print("")
        
        for line in draw:
            print(line)

        print(f"\n{points}\n")

        
board = Board(10, 10, 6, 3)
board.print()