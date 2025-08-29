import time
import GetchFunctions

# Config #

ConsiderEnterKeystroke = True
LogLevel = 1
NAttempts = 2
EpsilonTimingVector = []

# #

def PrintTimingMatrix(matrix):
    print("\n".join(["->".join([str(Value) for Value in Vector]) for Vector in matrix]))

def main():
    getch = GetchFunctions._Getch()

    RawTimingVectors = [] # ns Timestamps of each keystroke
    DiffTimingVectors = [] # ns time between the last and the current keystroke

    for AttemptIdx in range(NAttempts):
        EnteredPasswordBytes = []
        InChar = b''
        RawTimingVectors.append([])
        ##KeyStrokeIdx = 0
        while InChar != b'\r' and InChar != b'\n':
            EnteredPasswordBytes.append(InChar) # Adds to Keystroke-Timing, can be moved outside of loop! (TODO)
            InChar = getch()                    # Adds to Keystroke-Timing
            RawTimingVectors[AttemptIdx].append(time.time_ns()) # Also measuring timing of "Enter" keystroke
            ##KeyStrokeIdx += 1                   # Adds to Keystroke-Timing
            
        EnteredPasswordString = b''.join(EnteredPasswordBytes).decode()
        print(f"{AttemptIdx+1}: {EnteredPasswordString}")

    if LogLevel > 0:
        print("Raw Timing Vectors:")
        PrintTimingMatrix(RawTimingVectors)

    for AttemptIdx in range(NAttempts): # TODO: Make this a function (its not vector-difference, is it eucledian distance?)
        DiffTimingVectors.append([])
        for KeyStrokeIdx in range(1, len(RawTimingVectors[AttemptIdx])):
            KeyStrokeTimingDifference = RawTimingVectors[AttemptIdx][KeyStrokeIdx] - RawTimingVectors[AttemptIdx][KeyStrokeIdx - 1]
            DiffTimingVectors[AttemptIdx].append(KeyStrokeTimingDifference)
            
    if LogLevel > 0:
        print("Difference Timing Vectors:")
        PrintTimingMatrix(DiffTimingVectors)

if __name__ == "__main__":
    main()