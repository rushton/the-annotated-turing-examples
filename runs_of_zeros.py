"""
From page 87

b  --  nil            --  Pe,R,Pe,R,P0,R,R,P0,L,L  --  D
D  --  0,1            --  R,Px,L,L,L               --  D,q
q  --  Any(0,1),None  --  R,R|P1,L                 --  q,p
p  --  x,e,None       --  E,R|R|L,L                --  q,f,p
f  --  Any,None       --  R,R|P0,L,L               --  f,D
"""

from tape import Tape, TapeRanOutException

def runs_of_zeros():
    tape = Tape(max_length=100)
    try:
        begin(tape)
    except TapeRanOutException:
        print(tape)

def begin(tape: Tape):
    print("config begin")
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
    """
    D  --  1,0            --  R,Px,L,L,L               --  D,q
    """
    print("config D")
    if tape.is_one():
        tape.move_right()
        tape.print_x()
        tape.move_left(3)
        config_D(tape)
        return
    if tape.is_zero():
        config_q(tape)
        return
    raise Exception(f"Invalid state in config D tape:\n{tape}")

def config_q(tape: Tape):
    print("config q")
    if tape.is_zero() or tape.is_one():
        tape.move_right(2)
        config_q(tape)
        return
    if tape.is_empty():
        tape.print_one()
        tape.move_left()
        config_p(tape)
        return

    raise Exception(f"Invalid state in config q, tape:\n {tape}")


def config_p(tape: Tape):
    """
    p  --  x,e,None       --  E,R|R|L,L                --  q,f,p
    """
    print("config p")
    if tape.is_x():
        tape.erase()
        tape.move_right()
        config_q(tape)
        return
    if tape.is_schwa():
        tape.move_right()
        config_f(tape)
        return
    if tape.is_empty():
        tape.move_left(2)
        config_p(tape)
        return
    raise Exception(f"Invalid state in config p, tape:\n{tape}")

def config_f(tape: Tape):
    """
    f  --  Any,None       --  R,R|P0,L,L               --  f,D
    """
    print("config f")
    if tape.is_one() or tape.is_zero():
        tape.move_right(2)
        config_f(tape)
        return
    if tape.is_empty():
        tape.print_zero()
        tape.move_left(2)
        config_D(tape)
        return
    raise Exception(f"Invalid state in config f, tape:\n{tape}")

    
def main():
    runs_of_zeros()

if __name__ == '__main__':
    main()
