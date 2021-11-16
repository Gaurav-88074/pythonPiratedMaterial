def evenTuple(userTuple):
    res = [i for i in userTuple if i % 2 == 0]
    return tuple(res)


def concat(firstTuple, secondTuple):
    res = [i for i in firstTuple]
    res.extend([i for i in secondTuple])
    return tuple(res)


def maxAndMin(userTuple):
    res = list(userTuple)
    return (max(res), min(res))


# Driver Code
userTuple = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
secondTuple = (11, 13, 15)

print(f"Even Tuple : {evenTuple(userTuple)}")
userTuple = concat(userTuple, secondTuple)
print(f"Concated Tuple : {userTuple}")

maxValue, minValue = maxAndMin(userTuple)
print(f"Min Value : {minValue}")
print(f"Max Value : {maxValue}")
