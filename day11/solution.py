"""
Solutions to Day 11 of Advent of Code by Alvaro Clemente
"""


def parse_input(filename="input.txt"):
    """
    The answers for a group are in a block (delimited by empty lines)
    For each group the answers for each person are in a line
    """
    board = []
    with open(filename, "r") as f:
        for line in f.readlines():
            row = [c for c in line.strip()]
            board.append(row)
    return board


# Parsed input
board = parse_input()

# Solution for #1
class GameOfThrones:
    """
    Definitely not a Game of Life
    """

    EMPTY = "L"
    OCCUPIED = "#"
    FLOOR = "."

    def __init__(self, initial, n_to_occupy=0, n_to_free=4):
        self.board = initial
        self.rows = len(initial)
        self.cols = len(initial[0])  # We assume the board is regular
        self.n_to_occupy = n_to_occupy
        self.n_to_free = n_to_free

    def run(self):
        """Run until the board is stable"""
        while True:
            changed = self.run_next()
            if not changed:
                return

    def run_next(self):
        """Simulate a single round"""
        new_board = [[""] * self.cols for _ in range(self.rows)]
        for x in range(self.cols):
            for y in range(self.rows):
                new_seat = self._simulate_seat(x, y)
                new_board[y][x] = new_seat
        changed = self._board_changed(new_board)
        self.board = new_board
        return changed

    def _simulate_seat(self, x, y):
        """Evaluate the rules"""
        seat = self.board[y][x]
        if seat == ".":
            return "."
        elif seat == "L":
            n_adjacent = self._count_adjacent(x, y)
            return "#" if n_adjacent == self.n_to_occupy else "L"
        else:
            n_adjacent = self._count_adjacent(x, y)
            return "L" if n_adjacent >= self.n_to_free else "#"

    def _count_adjacent(self, x, y):
        """Count the number of adjacent occupied seats"""
        top_left = self.board[y - 1][x - 1] if y > 0 and x > 0 else "."
        top = self.board[y - 1][x] if y > 0 else "."
        top_right = self.board[y - 1][x + 1] if y > 0 and x < (self.cols - 1) else "."
        center_left = self.board[y][x - 1] if x > 0 else "."
        center_right = self.board[y][x + 1] if x < (self.cols - 1) else "."
        bottom_left = self.board[y + 1][x - 1] if y < (self.rows - 1) and x > 0 else "."
        bottom = self.board[y + 1][x] if y < (self.rows - 1) else "."
        bottom_right = (
            self.board[y + 1][x + 1]
            if y < (self.rows - 1) and x < (self.cols - 1)
            else "."
        )
        adjacent = [
            top_left,
            top,
            top_right,
            center_left,
            center_right,
            bottom_left,
            bottom,
            bottom_right,
        ]
        return sum(1 for seat in adjacent if seat == self.OCCUPIED)

    def count_occupied(self):
        return sum(1 for row in self.board for seat in row if seat == "#")

    def _board_changed(self, new):
        """Checks if the board has changed"""
        return any(self.board[i] != new[i] for i in range(self.rows))

    def print_board(self):
        board_string = "\n".join("".join(row) for row in self.board)
        print(board_string)


game = GameOfThrones(board)
game.run()
print(game.count_occupied())


# Solution for #2
class GameOfThronesv2(GameOfThrones):
    """The second version of the awesome game of seats"""

    FRONT = 1
    CENTER = 0
    BACK = -1

    def __init__(self, initial, n_to_occupy=0, n_to_free=5, *args, **kwargs):
        super().__init__(
            initial, n_to_occupy=n_to_occupy, n_to_free=n_to_free, *args, **kwargs
        )

    def _count_adjacent(self, x, y):
        # TODO(alvaro): Use here line of sight instead of adjacency
        top_left = self._seat_in_sight(x, y, xdirection=self.BACK, ydirection=self.BACK)
        top = self._seat_in_sight(x, y, xdirection=self.CENTER, ydirection=self.BACK)
        top_right = self._seat_in_sight(
            x, y, xdirection=self.FRONT, ydirection=self.BACK
        )
        center_left = self._seat_in_sight(
            x, y, xdirection=self.BACK, ydirection=self.CENTER
        )
        center_right = self._seat_in_sight(
            x, y, xdirection=self.FRONT, ydirection=self.CENTER
        )
        bottom_left = self._seat_in_sight(
            x, y, xdirection=self.BACK, ydirection=self.FRONT
        )
        bottom = self._seat_in_sight(
            x, y, xdirection=self.CENTER, ydirection=self.FRONT
        )
        bottom_right = self._seat_in_sight(
            x, y, xdirection=self.FRONT, ydirection=self.FRONT
        )
        adjacent = [
            top_left,
            top,
            top_right,
            center_left,
            center_right,
            bottom_left,
            bottom,
            bottom_right,
        ]
        return sum(1 for seat in adjacent if seat == self.OCCUPIED)

    def _seat_in_sight(self, x, y, xdirection=CENTER, ydirection=CENTER):
        """
        Check the seats in the line of sight

        The directions for each axis are:
            X:
                FRONT == right (higher col index)
                CENTER == center (same col index)
                BACK == left (lower col index)
            Y:
                FRONT == bottom (higher col index)
                CENTER == center (same col index)
                BACK == up (lower col index)
        """
        assert not (
            xdirection == self.CENTER and ydirection == self.CENTER
        ), "The must not be both 0"
        cur_x, cur_y = x, y
        while True:
            cur_x += xdirection
            if cur_x < 0 or cur_x >= self.cols:
                # Got to the end
                break
            cur_y += ydirection
            if cur_y < 0 or cur_y >= self.rows:
                # Got to the end
                break
            cur_seat = self.board[cur_y][cur_x]
            if cur_seat != self.FLOOR:
                return cur_seat
        return self.FLOOR


game2 = GameOfThronesv2(board)
game2.run()
print(game2.count_occupied())

# Test
test_board = parse_input("input_test.txt")
test_game = GameOfThrones(test_board)
test_game.run_next()
print(test_game.count_occupied())
test_game.print_board()

test_game.run()

test_game2 = GameOfThronesv2(test_board)
test_game2.run_next()
print(test_game2.count_occupied())
test_game2.print_board()

test_game2.run()
print(test_game2.count_occupied())
