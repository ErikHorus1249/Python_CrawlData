

class TikiTarget:
    def __init__(self, patternsStr="", categoryStr=""):
        self.patternsString = patternsStr 
        self.patterns = []
        self.categoryUrl = categoryStr

    def info(self):
        return "patterns : " + self.patternsString + "categoriesUrl : "+self.categoryUrl