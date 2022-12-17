import requests
import json 

#requests simple

url= "https://rickandmortyapi.com/api/character/200"
r=requests.get(url)
j= r.json()



status = j['status']
print(status)

i = 1 
while 1 < 11:
    url ='https://rickandmortyapi.com/api/character/{}'.format(i)
    r=requests.get(url)
    j= r.json()
    name = j['name']
    status = j['status']
    print ('El personaje {} tiene status : {}'.format(name,status))
    i+=1
