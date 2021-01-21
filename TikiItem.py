
class TikiItem :
    # init function()
    def __init__(self):
        self.title = ""
        self.price = 0
        self.regularPrice = 0
        self.url = ""
    #check input 
    def info(self):
        return str(self.title) + "| " + str(self.regularPrice) + "|" + str(self.url) 