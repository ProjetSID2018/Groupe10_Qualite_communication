#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 08:58:19 2018
# Group 4
# Realized by DELOEUVRE Noémie
"""

from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re
import os
import g4_utils_v32 as utils


def articles_category(cat):
    # We retrieve the URL feeds for each page of article
    # Each HTML-coded article is analyzed with beautiful soup
    for i in range(2, 10):
        url_rss_humanite = "https://humanite.fr/" + cat + "?page=" + str(i) + "/feed/"
        req = requests.get(url_rss_humanite)
        data = req.text
        soup_url = BeautifulSoup(data, "lxml")
        articles_humanite = []
        # We retrieve all the articles for a given page
        for div in soup_url.find_all('div'):
            for valeur in re.finditer('field-name-field-news-chapo', str(div.get("class"))):
                for a in div.find_all('a'):
                    articles_humanite.append(a.get("href"))
    return articles_humanite

def file_Json(list_category):
    fileJson_all = []
    for cat in list_category:
        articles_humanite = articles_category(cat)
        # Each article is analized one by one
        for article in articles_humanite:
            req = requests.get(article)
            data = req.text
            soup = BeautifulSoup(data, "lxml")
            # Retrieving of title
            for meta in soup.find_all('meta'):
                if meta.get("property") == 'og:title':
                    title = meta.get("content")
            # Retrieving of the newspaper name
            for meta in soup.find_all('meta'):
                if meta.get("property") == 'og:site_name':
                    newspaper = meta.get("content")
            # Retrieving of the theme
            for meta in soup.find_all('meta'):
                if meta.get("property") == 'article:section':
                    theme = meta.get("content")
            # Retrieving of the author
    
            author = []
            for h2 in soup.find_all('h2'):
                for a in h2.find_all('a'):
                    for valeur in re.finditer('auteur', str(a.get("href"))):
                        author.append(a.get_text())
                        """
            for div in soup.find_all('div', class_="field field-name-field-news-auteur-nom-trias field-type-text field-label-hidden"):
                for d in div.find_all("div", class_="field-item even"):
                    author = d.get_text()
                    """
            # Retrieving of the date of publication
            for meta in soup.find_all('meta'):
                if meta.get("property") == 'article:published_time':
                    raw_date = meta.get("content")
                    date_p = raw_date[0:10]
                    date_p = datetime.strptime(date_p, "%Y-%m-%d").strftime("%d/%m/%Y")
            # Retrieving the content of the article
            contents = ""
            for p in soup.find_all('p'):
                for a in p.find_all('a'):
                    if a.get_text() == "Lire la suite":
                        a.string = ""
                if p.get("class") == ['TX']:
                    contents += p.get_text()
            new_article = {
                "title": title,
                "newspaper": newspaper,
                "date_publi": date_p,
                "author": author,
                "theme": theme,
                "content": contents
            }
            fileJson_all.append(new_article)
    return fileJson_all


def recuperation_info_hmnt(file_target = "/Users/nabil/Desktop/Projet/humanite"):
    # os.makedirs(file_target, exist_ok=True)
    list_category = ["politique", "société", "social-eco", "culture", "sports",
                 "monde", "environnement", "rubriques/en-debat"]
    files_json = file_Json(list_category)
    len(files_json)
    sources = "Humanite/"
    if not os.path.exists(file_target+sources):
        os.makedirs(file_target+sources)
    # Call the create_json function
    utils.create_json(file_target, files_json, sources, "hum")


if __name__ == '__main__':
    recuperation_info_hmnt()
