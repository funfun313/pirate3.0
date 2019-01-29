import json
from firebase import firebase as fb
class FirebaseManager:
    app = fb.FirebaseApplication("https://piratedb-9296e.firebaseio.com", None)
    
    def writenewobject(self,id,d):
        self.app.put("", id, d)
    def getallpirates(self):
        d = self.app.get("", None)
        return d
