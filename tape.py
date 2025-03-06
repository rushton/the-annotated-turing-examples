class Tape:
    def __init__(self):
        self.tape = [" "]
        self.position = 0

    def move_left(self, spaces=1):
        self.position -= spaces

    def move_right(self, spaces=1):
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
        self.tape[self.position] = ""

    def is_empty(self):
        return self.tape[self.position] == " "

    def is_one(self):
        return self.tape[self.position] == "1"

    def is_zero(self):
        return self.tape[self.position] == "0"

    def is_schwa(self):
        return self.tape[self.position] == "e"

    def print_tape(self):
        print("| " + " | ".join(self.tape) + " |")
        print((" " * 4 * self.position) + "  " + "^")
