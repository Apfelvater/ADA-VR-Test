import time
import GetchFunctions
import string
import sys
from Utility import *

# Config #

ConsiderEnterKeystroke = False
LogLevel = 2
NAttempts = 2
EpsilonEuclideanDistanceNS = 0.69 * 10**9

# #

def RequestPassword(considerEnterKeystroke, getch):
    EnteredPasswordBytes = []
    RawKeystrokeTimingVector = []
    InChar = b''
    while InChar != b'\r' and InChar != b'\n':

        # If character is not printable, we ingore it and take the time from this keystroke to the next one
        # Therefore we overwrite the last keystroke timing
        if InChar.decode() not in string.printable: # Adds to Keystroke-Timing
            InChar = getch()                # Adds to Keystroke-Timing
            RawKeystrokeTimingVector[-1] = time.time_ns()
            continue

        EnteredPasswordBytes.append(InChar) # Adds to Keystroke-Timing
        InChar = getch()                    # Adds to Keystroke-Timing

        RawKeystrokeTimingVector.append(time.time_ns()) # Also measuring timing of "Enter" keystroke
        
    EnteredPasswordString = b''.join(EnteredPasswordBytes).decode()

    if not considerEnterKeystroke:
        RawKeystrokeTimingVector = RawKeystrokeTimingVector[:-1]

    return EnteredPasswordString, RawKeystrokeTimingVector

def RequestEnrollment(nAttempts, considerEnterKeystroke, getch):

    print("Enter your password for enrollment (5 attempts):")

    RawTimingVectors = [] # All vectors of ns Timestamps of each keystroke
    DiffTimingVectors = [] # All vectors of ns time between the last and the current keystroke
    EnteredPasswordString = None

    for AttemptIdx in range(nAttempts):
        RawTimingVectors.append([])
        
        NextEnteredPasswordString, RawKeystrokeTimingVector = RequestPassword(considerEnterKeystroke, getch)

        RawTimingVectors[AttemptIdx] = RawKeystrokeTimingVector

        print(f"Attempt {AttemptIdx+1}: {NextEnteredPasswordString}")

        if EnteredPasswordString != None and NextEnteredPasswordString != EnteredPasswordString:
            raise Exception("Password doesnt match. Enrollment process failed!")
        
        EnteredPasswordString = NextEnteredPasswordString

    if LogLevel > 1:
        print("Raw Timing Vectors:")
        PrintTimingMatrix(RawTimingVectors)

    for AttemptIdx in range(nAttempts):
        DiffTimingVectors.append(DiffTimingVector(RawTimingVectors[AttemptIdx]))
    
    if LogLevel > 0:
        print("Difference Timing Vectors:")
        PrintTimingMatrix(DiffTimingVectors)

    return EnteredPasswordString, AverageVector(*DiffTimingVectors)

def main():
    getch = GetchFunctions._Getch()

    try:
        EnrollmentPassword, AverageTimingVector = RequestEnrollment(NAttempts, ConsiderEnterKeystroke, getch)
    except Exception as e:
        print(e)
        return False

    if LogLevel > 0:
        print("Enrollment Average Timing Vector:")
        print("->".join([str(Time) for Time in AverageTimingVector]))
        print()

    print("(login phase)")

    print("Enter your password: ", end="")
    sys.stdout.flush()
    LoginAttemptPasswordString, LoginAttemptRawTimingVector = RequestPassword(ConsiderEnterKeystroke, getch)
    print(LoginAttemptPasswordString)
    LoginAttemptDiffTimingVector = DiffTimingVector(LoginAttemptRawTimingVector)

    if LoginAttemptPasswordString != EnrollmentPassword:
        print("Password incorrect!")
        return False

    if LogLevel > 0:
        print("Login Attempt Diff Timing Vector:")
        print("->".join([str(Time) for Time in LoginAttemptDiffTimingVector]))
        print()

    LoginAttemptEuclideanDistance = EuclideanDistance(LoginAttemptDiffTimingVector, AverageTimingVector)

    if LogLevel > 1:
        print("Euclidean Distance (Login Attempt <-> Enrollment Average):")
        print(LoginAttemptEuclideanDistance)
        print()

    if LoginAttemptEuclideanDistance <= EpsilonEuclideanDistanceNS:
        print("Access granted!")
        return True
    else:
        print("Access denied!")
        return False

if __name__ == "__main__":
    main()