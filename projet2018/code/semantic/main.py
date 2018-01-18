import glob
import time
import requests
import sys
sys.path.insert(0, 'Article_analysis/Polarity')

import g6_polarity_voting_v1_2 as lib
from Word_analysis import g6_create_file_wiki_syno as create
import json

SERVER_URL = 'http://130.120.8.250:5005/var/www/html/projet2018/code/bd_index/API/index/'  # change this url with server url
SERVER_PATH_FILTERING = '/var/www/html/projet2018/data/clean/filtering/*.json'

if __name__ == '__main__':

    skipped_files = []

    for file in glob.glob(SERVER_PATH_FILTERING):
        start = time.time()
        out_file = lib.in_polarity_out(file)
        print("Etape 1 polarity : ", time.time() - start)
        #payload = out_file
        payload = []
        payload.append(out_file)
#        payload = json.dumps(payload, ensure_ascii=False)
        response = requests.post(SERVER_URL+'article', json=payload)
        print(response)
        print(response.json())
        
        if response.status_code != 200:
            skipped_files.append(file)
            continue
        else:
            id_article = response.json()[0]["message"]["id_article"]
            start2 = time.time()            
            word_list = create.create_wiki_syno(file, id_article)
            #payload2 = []
            print("Etape 2 synonymes : ", time.time() - start2)
            payload2 = word_list
            print(payload2)
            requests.post(SERVER_URL+'positionword', json=payload2)
            print(response)
            

        article = response.json()
        print(skipped_files)
