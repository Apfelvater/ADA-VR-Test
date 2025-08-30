# Utility and Math functions

import math

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
