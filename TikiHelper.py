from TikiTarget import TikiTarget

def getTargetFromFile(fileName):
    targetFile = open(fileName,"r")
    lines = targetFile.readlines()
    targetFile.close()

    targets = []
    n = len(lines)
    
    print(n)
    i = 0
    while i < n-1:
        newTarget = TikiTarget(lines[i].strip(),lines[i+1].strip())
        # print(newTarget.info())
        targets.append(newTarget)
        i += 2
    return targets
    print("----End----")
