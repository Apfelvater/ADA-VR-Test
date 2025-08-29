import time

# Config #

Debug = True
NAttempts = 2
EpsilonTimingVector = []

# #

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

RawTimingVectors = [] # ns Timestamps of each keystroke
DifTimingVectors = [] # ns time between the last and the current keystroke

for AttemptIdx in range(NAttempts):
    EnteredPasswordBytes = []
    InChar = b''
    RawTimingVectors.append([])
    ##KeyStrokeIdx = 0
    while InChar != b'\r' and InChar != b'\n':
        EnteredPasswordBytes.append(InChar) # Adds to Keystroke-Timing
        InChar = getch()                    # Adds to Keystroke-Timing
        RawTimingVectors[AttemptIdx].append(time.time_ns())
        ##KeyStrokeIdx += 1                   # Adds to Keystroke-Timing
        
    EnteredPasswordString = b''.join(EnteredPasswordBytes).decode()
    print(f"{AttemptIdx+1}: {EnteredPasswordString}")

if Debug:
    print("Raw Timing Vectors:")
    print("\n".join(["->".join([str(TimeStamp) for TimeStamp in Attempt]) for Attempt in RawTimingVectors]))

