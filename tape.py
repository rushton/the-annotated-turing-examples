import sys


class TapeRanOutException(Exception):
    pass

class Tape:
    def __init__(self, max_length=10):
        self.tape = [" "]
        self.position = 0
        self.max_length = max_length

    def move_left(self, spaces=1):
        self.position -= spaces

    def move_right(self, spaces=1):
        if len(self.tape) + spaces > self.max_length:
            raise TapeRanOutException()

        self.position += spaces
        if len(self.tape) <= self.position:
            for idx in range(spaces):
                self.tape.append(" ")

    def print_one(self):
        self.tape[self.position] = "1"

    def print_zero(self):
        self.tape[self.position] = "0"

    def print_schwa(self):
        self.tape[self.position] = "e"

    def print_x(self):
        self.tape[self.position] = "x"

    def read(self):
        return self.tape[self.position]

    def erase(self):
        self.tape[self.position] = " "

    def is_empty(self):
        return self.tape[self.position] == " "

    def is_one(self):
        return self.tape[self.position] == "1"

    def is_zero(self):
        return self.tape[self.position] == "0"

    def is_schwa(self):
        return self.tape[self.position] == "e"

    def is_x(self):
        return self.tape[self.position] == "x"

    def print_tape(self):
        print(self)

    def __str__(self):
        s = self._get_selected_char(1) + " "
        for idx, itm in enumerate(self.tape):
            surround = self._get_selected_char(idx)
            s+= itm
            if (idx+1) % 25 == 0:
                s += '\n'
            else:
                s += ' '
            s += surround + " "

        return s
    def _get_selected_char(self, idx):
        if self.position == idx or self.position + 1 == idx:
            return '*'
        else:
            return '|'
