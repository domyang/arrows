SAMPLE = """v<^><>>v><>^<>vvv^^>
>^<>^<<v<>>^v^v><^<<
v^^>>>>>><v^^<^vvv>v
^^><v<^^<^<^^>>>v>v>
^<>vv^><>^<^^<<^^><v
^vv<<<><>>>>^<>^^^v^
^<^^<^>v<v^<>vv<^v<>
v<>^vv<^>vv>v><v^>^^
>v<v><^><<v>^^>>^<>^
^v<>^<>^>^^^vv^v>>^<
v>v^^<>><<<^^><^vvv^"""

directions = {
    '^': 'up',
    '>': 'right',
    '<': 'left',
    'v': 'down'
}

class Path:
    def __init__(self):
        pass

    def find_loop(self):
        pass

class Cell:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = directions[direction]

    def __repr__(self):
        return "<Cell ({},{}) '{}'>".format(self.x, self.y, self.direction)


class Grid:
    def __init__(self, grid):
        self.grid = []
        for y, col in enumerate(grid.split('\n')):
            row = []
            for x, char in enumerate(col):
                row.append(Cell(x, y, char))
            self.grid.append(row)

    def get_cell(self, x, y):
        return self.grid[y][x]

    def generate_paths(self):
        pass

    def find_loops(self):
        pass

    def __str__(self):
        return str(self.grid)

    def find_largest_loop(self):
        pass

if __name__ == '__main__':
    grid = Grid(SAMPLE)
    print(grid.get_cell(5, 5))