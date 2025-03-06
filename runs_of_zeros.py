"""
From page 87

b  --  nil            --  Pe,R,Pe,R,P0,R,R,P0,L,L  --  D
D  --  0,1            --  R,Px,L,L,L               --  D,q
q  --  Any(0,1),None  --  R,R|P1,L                 --  q,p
p  --  x,e,None       --  E,R|R|L,L                --  q,f,p
f  --  Any,None       --  R,R|P0,L,L               --  f,D
"""

from tape import Tape

def runs_of_zeros():
    tape = Tape()
    begin(tape)

def begin(tape: Tape):
    tape.print_schwa()
    tape.move_right()
    tape.print_schwa()
    tape.move_right()
    tape.print_zero()
    tape.move_right(2)
    tape.print_zero()
    tape.move_left(2)
    config_D(tape)

def config_D(tape: Tape):
    if tape.is_zero():
        tape.move_right()
        tape.print_x()
        tape.move_left(3)
        config_D(tape)
        return
    if tape.is_one():
        config_q(tape)
        return
    raise Exception("Invalid state in config D")

def config_q(tape: Tape):
    if tape.is_zero() or tape.is_one():
        tape.move_right(2)
        config_q(tape)
        return
    if tape.is_empty():
        tape.print_one()
        tape.move_left()
        config_p(tape)
        return

    raise Exception("Invalid state in config q")


def config_p(tape: Tape):
    """
    p  --  x,e,None       --  E,R|R|L,L                --  q,f,p
    """
    if tape.is_x():
        tape.erase()
        tape.move_right()
        config_q(tape)
        return
    if tape.is_schwa():
        tape.move_right()
        config_f(tape)
        return
    if tape.is_none():
        tape.move_left(2)
        config_p(tape)
        return
    raise Exception("Invalid state in config p")


def main():
    pass

if __name__ == '__main__':
    main()
