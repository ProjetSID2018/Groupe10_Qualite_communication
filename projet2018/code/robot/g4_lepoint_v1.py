# -*- coding: utf-8 -*-
# Authors : Noemie DELOEUVRE, Morgan SEGUELA, Celine Mothes, Aurelien PELAT
# Version : 1.0

import datetime as date
from bs4 import BeautifulSoup
import requests
import re
import g4_utils_v32 as utils


def collect_url_themes(soup):
    """
    """
    list_url_themes = []
    # Creation de la liste des themes disponibles
    for li in soup.find_all('li'):
        if li.get("class") == ['header-red-li']:
            for a in li.find_all('a'):
                if (a.get("href") != '/video/'
                        and a.get("href") != 'http://afrique.lepoint.fr'
                        and a.get("href") != '/edition-abonnes/'):
                    list_url_themes.append('http://www.lepoint.fr' +
                                           a.get("href"))
    return list_url_themes


def collect_url_articles(url_articles, url_theme):
    """
    """
    # Parsing de la page du theme avec Beautiful Soup
    req = requests.get(url_theme)
    data = req.text
    soup = BeautifulSoup(data, "lxml")

    for div in soup.find_all('div'):
        if div.get('class') == ['list-view']:
            for a in div.find_all('a'):
                if ('http' in a.get('href')
                        and a.get('href') not in url_articles):
                    url_articles.append(a.get('href'))
                elif ('http' not in a.get('href')
                        and 'http://www.lepoint.fr' + a.get('href')
                        not in url_articles):
                    url_articles.append('http://www.lepoint.fr'+a.get('href'))


def collect_articles(list_dictionnaires, list_url_articles, theme):
    """
    """
    # Parcours des articles du theme
    for url_article in list_url_articles:

        # Parsing de l article avec Beautiful Soup
        req = requests.get(url_article)
        data = req.text
        soup = BeautifulSoup(data, "lxml")

        # Recuperation du titre
        balise_title = soup.title.string
        sep = balise_title.split(" - Le Point")
        titre = sep[0]

        # Recuperation de la liste des auteurs de l article
        auteur = []
        for a in soup.find_all('a'):
            if a.get('class') == ['show-author']:
                auteur.append(a.get_text())
        # "\s\s+", "",

        # Recuperation dela date de publication et eventuellement d une date
        # de modification
        dates = []
        for time in soup.find_all('time'):
            for valeur in re.finditer('[0-9]{2}\/[0-9]{2}\/[0-9]{4}',
                                      str(time)):
                dates.append(date.datetime.strptime(valeur.group(0),
                                                    '%d/%m/%Y'))

        # Recuperation de la date de publication de l article
        date_p = date.datetime.strftime(min(dates), '%d/%m/%Y')

        # Recuperation du contenu de l article
        contenu = ""
        for h2 in soup.find_all('h2'):
            if h2.get('class') == ['art-chapeau']:
                contenu += h2.get_text()+" "

        for div in soup.find_all('div'):
            if div.get('class') == ['art-text']:
                for p in div.find_all('p'):
                    contenu += p.get_text()+" "

        new_article = {
                "title": titre,
                "newspaper": 'Le Point.fr',
                "author": auteur,
                "date_publi": date_p,
                "content": contenu,
                "theme": theme
        }

        # Ajout de l article a la liste d articles
        list_dictionnaires.append(new_article)

# data/clean/robot/


def recovery_new_articles_lpt(
        file_target="C:/Users/aurel/Documents/Etudes/ProjetIPJournaux" +
        str(date.datetime.now().date()) + "/"):
    """
    """
    # Adresse url Le Point
    url_lepoint = 'http://www.lepoint.fr/'

    # Parsing de la page d accueil avec Beautiful Soup
    req = requests.get(url_lepoint)
    data = req.text
    soup = BeautifulSoup(data, "lxml")

    list_url_themes = collect_url_themes(soup)

    # Creation de la liste d articles du theme
    list_url_articles = []
    # Creation de la liste des articles
    list_dictionnaires = []
    # Parcours des themes
    for url_theme in list_url_themes:
        # Recuperation du theme
        theme = re.search("http://www.lepoint.fr/(.*)/", url_theme)[1]
        # Collecte des url des articles
        collect_url_articles(list_url_articles, url_theme)
        for index_page in range(2, 10):
            collect_url_articles(list_url_articles,
                                 url_theme+"index_"+str(index_page)+".php")
        # Collecte des articles
        collect_articles(list_dictionnaires, list_url_articles, theme)

    utils.create_json(file_target, list_dictionnaires, "LePointExistant/",
                      "lpt")


if __name__ == '__main__':
    recovery_new_articles_lpt()
