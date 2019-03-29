from google.cloud import storage
import os, datetime

class ImageManager:
    #this is a credential file for google
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

    client = storage.Client()
    bucket = client.get_bucket("piratedb-9296e.appspot.com")

    imagepath = "pirate2.gif"
    url = ""
    
    def uploadImage(self):
        imageBlob = bucket.blob("images/" + self.imagepath)
        imageBlob.upload_from_filename(self.imagepath)
        d = datetime.datetime(2040,1,1)
        self.url = imageBlob.generate_signed_url(d)
