import json
class FileManager:
    path = "pirate.json"
    def writenewobject(self,id,d):
        try:
            #try to open file and read it to a dict
            f = open(self.path,"r")
            d2 = json.load(f)
            f.close()
        except:
            d2= {}
        d2[id]= d
        f=open(self.path,"w")
        json.dump(d2,f)
        f.close()
        
