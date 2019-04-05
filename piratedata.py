class Pirate:
    name = ""
    ship = ""
    fictional = ""
    image = ""
    def getdict(self):
        d = {"name":self.name,"ship":self.ship,"fictional":self.fictional, "image":self.image}
        return d
    def loadfromdict(self,d):
        self.name = d["name"]
        self.ship = d["ship"]
        self.fictional = d["fictional"]
        self.image = d["image"]
