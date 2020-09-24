

class TikiTarget:
    def __init__(self, patternsStr="", categoryStr=""):
        self.patternsString = patternsStr 
        self.patterns = self.__SplitPattern()
        self.categoryUrl = categoryStr

    def info(self):
        return "patterns : " + str(self.patterns[1]) + "categoriesUrl : "+self.categoryUrl
    
    def __SplitPattern(self):
        newList = self.patternsString.split(",")
        i = 0
        while i < len(newList):
            newList[i] = newList[i].strip()
            i += 1
        return newList