# Complete the marsExploration function below.
def marsExploration(s):
    iterations, cntViolations = len(s)//3, 0
    for iteration in range(iterations):
        subStr = s[(iteration*3):(iteration*3+3)]
        print(subStr)
        if subStr[0]!='S':
            cntViolations += 1
        if subStr[1] != 'O':
            cntViolations += 1
        if subStr[2] != 'S':
            cntViolations += 1
    return cntViolations