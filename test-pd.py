from firebase import firebase as fb

app = fb.FirebaseApplication("https://piratedb-9296e.firebaseio.com", None)

#d = app.get("", "name")
#print(d)

newpirate = {"name":"Peter Pan", "ship":"Jolly Roger", "fictional":"true"}
newid= 44444
result = app.put("", newid, newpirate)
print(result)
