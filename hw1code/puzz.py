BLANK_CHAR = '0'


class EightPuzzleBoard:
    def __init__(self, board_string):
        self._board = list(board_string)

    def _get_tile(self, x, y):
        return self._board[6 - y * 3 + x]

    def _set_tile(self, x, y, val):
        self._board[6 - y * 3 + x] = val

    def success_move(self, delta_x, delta_y):
        pos = self._board.index(BLANK_CHAR)
        blank_x = pos % 3
        blank_y = 2 - int(pos / 3)
        move_x = blank_x + delta_x
        move_y = blank_y + delta_y
        if (move_x < 0) or (move_x > 2) or (move_y < 0) or (move_y > 2):
            return None
        else:
            succ = EightPuzzleBoard("".join(self._board))
            succ._set_tile(blank_x, blank_y, self._get_tile(move_x, move_y))
            succ._set_tile(move_x, move_y, self._get_tile(blank_x, blank_y))
            return succ

    def success_up(self):
        return self.success_move(0, -1)

    def success_down(self):
        return self.success_move(0, 1)

    def success_right(self):
        return self.success_move(-1, 0)

    def success_left(self):
        return self.success_move(1, 0)

    def successors(self):
        return { "up": self.success_up(),
                 "down": self.success_down(),
                 "left": self.success_left(),
                 "right": self.success_right() }

    def __str__(self):
        return "".join(self._board)

    def __repr__(self):
        return "".join(self._board)

    def pretty(self):
        brd_str = " ".join(self._board).replace(BLANK_CHAR, ".", 1)
        return "{}\n{}\n{}".format(brd_str[:6], brd_str[6:12], brd_str[12:])

    def __hash__(self):
        return hash("".join(self._board))

    def __eq__(self, other):
        return "".join(self._board) == "".join(other._board)







