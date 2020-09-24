
from TikiTarget import TikiTarget

TARGET_fILE = "target_list.txt"
targetFile = open(TARGET_fILE,"r")
lines = targetFile.readlines()
targetFile.close()

n = len(lines)

print(n)
i = 0
while i < n-1:
    newTarget = TikiTarget(lines[i].strip(),lines[i+1].strip())
    print(newTarget.info())
    i += 2

print("----End----")
# for line in lines:
#     # print(line.strip())
#     newLine = line.strip()
#     newTarget =  TikiTarget(newLine, newLine)
#     print(newTarget.info())
