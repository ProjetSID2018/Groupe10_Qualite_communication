# -*- coding: utf-8 -*-
# Groupe 4
# DELOEUVRE Noémie
# Céline MOTHES
# Morgan SEGUELA

import os
import json
import datetime as date
import csv
import re

def add_to_index(date, text, newspaper):
    hash_text = get_hash(date, text, newspaper)
    with open("hash_text.csv", "a") as f:
        f.write(hash_text + ",")

def get_hash(date, text, newspaper):
    """create a hash from the date, the title, and the newspaper to find if an article already exists
    
    Arguments:
        date {string} -- date of the article
        text {string} -- title of the article
        newspaper {string} -- name of the newspaper
    
    Returns:
        string -- a hash of the article
    """

    date = re.sub(r"/","",date)
    text = re.sub(r"\W", "", text)
    newspaper = re.sub(r"\W", "", newspaper)

    text = re.sub(r"[^bcdfghjklmnpqrstvwxz]", "", text)
    newspaper = re.sub(r"[^bcdfghjklmnpqrstvwxz]", "", newspaper)
    return date + text + newspaper

def already_exists(date, text, newspaper):
    """create a test to see if the article entered already exists
    
    Arguments:
        date {string} -- date of the article
        text {string} -- title of the article
        newspaper {string} -- name of the newspaper

    Returns:
        boolean -- False: Doesn't exist | True: Does exist
    """

    hash_text = get_hash(date, text, newspaper)
    with open("hash_text.csv", "r") as f:
        csv_reader = csv.reader(f, delimiter =",")
        already_existing_hash = csv_reader.__next__()[:-1]
    return hash_text in already_existing_hash

def create_index():
    """Create the index for all the article saved
    """    
    source = "data/clean/robot/"

    dates = os.listdir(source)
    
    hash_text = []

    for date in dates:
        source_date = source + date + "/"
        for newspaper in os.listdir(source_date):
            source_newpaper = source_date + newspaper + "/"

            for article in os.listdir(source_newpaper):
                with open(source_newpaper + article, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    title = data["title"]
                    date = data["date_publi"]
                    newspaper = data["newspaper"]

                hash_text.append(get_hash(date, title, newspaper))

    hash_text = list(set(hash_text))

    with open("hash_text.csv", "a") as f:
        f.write(",".join(hash_text)+",")


# Entree:
#   file_target: string containing the path of the folder
#   sources: string containing folder name
#   list_article: list containing new articles
#   abbreviation:string containing the journal abbreviation
# Exit:
#   one json file per item
# For each article, the function creates a json file named after it:
# art_abreviation_numeroArticle_datejour_robot. json.
# It places the json file in the folder corresponding to the journal
# if it exists otherwise it creates it.


def create_json(file_target, list_article, sources, abbreviation):
    if not os.path.exists(file_target+sources):
        os.makedirs(file_target+sources)
    i = 1
    cur_date = date.datetime.now().date()
    for article in list_article:
        if not already_exists(article["date_publi"], article["title"], article["newspaper"]):
            
            add_to_index(article["date_publi"], article["title"], article["newspaper"])

            if "/" in sources:
                file_art = file_target + sources + "art_" + abbreviation + "_"\
                    + str(i) + "_" + str(cur_date) + "_robot.json"
            else :
                file_art = file_target + sources + "/" + "art_" + abbreviation + "_"\
                    + str(i) + "_" + str(cur_date) + "_robot.json"

            with open(file_art, "w", encoding="UTF-8") as fic:
                json.dump(article, fic, ensure_ascii=False)

            i += 1

if __name__ == '__main__':
    create_index()
    print(already_exists("30092017dtrssdnglftntrjtllrgsprnbrvclvlbs"))
    


