# README

# 1. How To Run

python Main.py

# 2. Configuration

Hardcoded in "Main.py"
Default:
ConsiderEnterKeystroke = False              (The "Enter" keystroke will not be considered for time measurement)
LogLevel = 0                                (2 for full debug output)
NAttempts = 5                               (Number of enrollment attempts)
EpsilonEuclideanDistanceNS = 0.69 * 10**9   (Maximum euclidean distance between Login attempt and avg. enrollment attempt)

# 3. Required modules

These (standard python) modules are always imported:
math
string
sys

In Unix also required:
sys
tty
termios

In Windows also required:
msvcrt