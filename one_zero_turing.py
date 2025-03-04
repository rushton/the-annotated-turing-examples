from tape import Tape

def config_b(tape, iterations=10):
    if iterations == 0:
        return
    if tape.is_empty():
        tape.print_zero()
        config_b(tape, iterations-1)
    elif tape.is_zero():
        tape.move_right(2)
        tape.print_one()
        config_b(tape, iterations-1)
    elif tape.is_one():
        tape.move_right(2)
        tape.print_zero()
        config_b(tape, iterations-1)
    else:
        raise Exception("invalid state")

def print_alternating_one_zeros():
    tape = Tape()
    config_b(tape)
    tape.print_tape()

def main():
    print_alternating_one_zeros()

if __name__ == '__main__':
    main()
