
class TikiItem :
    def __init__(self):
        self.title = ""
        self.price = 0
        self.regularPrice = 0
        self.url = ""

    def info(self):
        return str(self.title) + "| " + str(self.regularPrice) + "|" + str(self.url) 