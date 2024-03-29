import requests
from concurrent.futures import ThreadPoolExecutor
import random, time

def do_post(n, url):
    files = {'file': open(n, 'rb')}
    data = {'files': 'file', "filename": n}
    print(" - POST " + str(n))
    return requests.post(url, files = files, data = data)

def main():
    num = input('Quantos pedidos em simultâneo? ')
    num = int(num)
    time_init = time.time()

    with ThreadPoolExecutor(max_workers=num) as pool:
        url='http://0.0.0.0/upload/'
        print(" Uploading " + str(num) + " random files: ")
        for i in range(num):
            filenum = random.randrange(90000, 90299)
            filenum = str(filenum)
            pool.submit(do_post,"client_files/0"+filenum+".jpg", url)
    time_end = time.time()
    resp_time = time_end - time_init
    print('Response Time: ' + str(resp_time))

main()