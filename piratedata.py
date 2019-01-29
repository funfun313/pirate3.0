class Pirate:
    name = ""
    ship = ""
    fictional = ""
    def getdict(self):
        d = {"name":self.name,"ship":self.ship,"fictional":self.fictional}
        return d
    def loadfromdict(self,d):
        self.name = d["name"]
        self.ship = d["ship"]
        self.fictional = d["fictional"]
        
