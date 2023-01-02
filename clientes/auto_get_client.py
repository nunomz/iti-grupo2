import aiohttp
import json
import requests
from concurrent.futures import ThreadPoolExecutor
import asyncio
import time

print("NAO ESQUECER DE APAGAR TUDO DO CLIENT_GETS ANTES DE CADA PEDIDO")

chunk_size = 64*1024*1024
dir = 'client_gets'

def listfiles():
    files = requests.get('http://0.0.0.0/list_files/').text
    return files

def do_get(fname, url):
    print(" - GETTING " + str(fname))
    payload = {'name': fname}
    response =  requests.get(url, payload).content
    filedir = dir+'/'+fname+'.zip'
    open(filedir, "wb").write(response)

ficheiros = listfiles()
#print(ficheiros)
# change the JSON string into a JSON object
jsonObject = json.loads(ficheiros)

num = input('Quantos pedidos em simultâneo? ')
num = int(num)

url='http://0.0.0.0/autodownload/'
time_init = time.time()

with ThreadPoolExecutor(max_workers=num) as pool:
    print(" Downloading " + str(num) + " random files: ")

    for i in range(num):
        value = jsonObject[i]
        pool.submit(do_get,value, url)
    time_end = time.time()
    resp_time = time_end - time_init
    print('Response Time: ' + str(resp_time))