import requests

class requests ():
   def __init__(self,url):
        self.url = url 


   def create_pastebin(self,data):
        r= requests.post(self.url,data)
        print (r.text)

req=requests('https://pastebin.com/api/api_post.php')

payload={'api_dev_key': 'UPF5SPmrDc8VbFMv5m1iNf8g0IeFcJaW' , 'api_paste_code': 'test','api_option':'paste'}

req.create_pastebin(payload)