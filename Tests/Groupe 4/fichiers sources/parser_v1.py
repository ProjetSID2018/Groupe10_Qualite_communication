"""
@author Morgan Seguela
V1 : Tout les journaux

!!!Non-complete version of the parser to make it easier to test!!!
"""
import datetime as date

import g4_new_gorafi_v1 as g4_gora


def activation(rss_function, newspaper):
    """active les fonctions de collecte

    Arguments:
        rss_function {func} -- Collecting Function
        newspaper {string} -- Newspaper Name
    """

    target_file = "/var/www/html/projet2018/data/clean/robot/" + \
        str(date.datetime.now().date()) + "/"

    # target_file = "data/clean/robot/" + str(date.datetime.now().date()) +"/"

    try:
        rss_function(target_file)
        print(newspaper + " OK")
    except Exception as exception:
        print(exception)
        print(type(exception).__name__)
        print("Erreur " + newspaper)


DEB = date.datetime.now()


activation(g4_gora.recovery_new_article_lg, "Le Gorafi")

DELTA = date.datetime.now() - DEB
print(DELTA.total_seconds())