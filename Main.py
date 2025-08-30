import math
import time
import GetchFunctions
import sys

# Config #

ConsiderEnterKeystroke = True
LogLevel = 2
NAttempts = 2
EpsilonEuclideanDistanceNS = 0.1 * 10**9

# #

def PrintTimingMatrix(matrix):
    print("\n".join(["->".join([str(Value) for Value in Vector]) for Vector in matrix]))
    print()

def EuclideanDistance(v1, v2):
    if len(v1) != len(v2):
        raise Exception("Vectors with unequal dimensions! Can't calculate euclidean distance.")
    SumOfSquares = 0
    for dim in range(len(v1)):
        SumOfSquares += (v1[dim] - v2[dim]) ** 2
    return math.sqrt(SumOfSquares)

def AverageVector(*vectors):
    # All vectors will have equal length, just trust me, ahem..
    AvgVector = [0] * len(vectors[0])
    for Vector in vectors:
        for i in range(len(AvgVector)):
            AvgVector[i] += Vector[i]
    for i in range(len(AvgVector)):
        AvgVector[i] = AvgVector[i] / len(vectors)
    return AvgVector

def DiffTimingVector(rawTimingVector):
    DiffTimingVector = []
    for KeyStrokeIdx in range(1, len(rawTimingVector)):
        KeyStrokeTimingDifference = rawTimingVector[KeyStrokeIdx] - rawTimingVector[KeyStrokeIdx - 1]
        DiffTimingVector.append(KeyStrokeTimingDifference)
    return DiffTimingVector

def RequestPassword(considerEnterKeystroke, getch):
    EnteredPasswordBytes = []
    RawKeystrokeTimingVector = []
    InChar = b''
    while InChar != b'\r' and InChar != b'\n':
        EnteredPasswordBytes.append(InChar) # Adds to Keystroke-Timing, can be moved outside of loop! (TODO)
        InChar = getch()                    # Adds to Keystroke-Timing
        RawKeystrokeTimingVector.append(time.time_ns()) # Also measuring timing of "Enter" keystroke
        
    EnteredPasswordString = b''.join(EnteredPasswordBytes).decode()

    if not considerEnterKeystroke:
        print("TODO remove last element of TimingVector")
        pass

    return EnteredPasswordString, RawKeystrokeTimingVector

def RequestEnrollment(nAttempts, considerEnterKeystroke, getch):

    print("Enter your password for enrollment (5 attempts):")

    RawTimingVectors = [] # ns Timestamps of each keystroke
    DiffTimingVectors = [] # ns time between the last and the current keystroke

    for AttemptIdx in range(nAttempts):
        RawTimingVectors.append([])
        
        EnteredPasswordString, RawKeystrokeTimingVector = RequestPassword(considerEnterKeystroke, getch)

        RawTimingVectors[AttemptIdx] = RawKeystrokeTimingVector

        print(f"Attempt {AttemptIdx+1}: {EnteredPasswordString}")

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

    EnrollmentPassword, AverageTimingVector = RequestEnrollment(NAttempts, ConsiderEnterKeystroke, getch)
    
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