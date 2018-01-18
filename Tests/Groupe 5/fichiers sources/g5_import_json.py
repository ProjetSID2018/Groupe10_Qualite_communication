"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan  9 15:45:27 2018
@group: Groupe 5 - Filtrage
@author: Cedric Bezy
Function : import and write json
============================================================================"""

from os import listdir
from re import findall
import json
from tqdm import tqdm
from datetime import datetime

"""============================================================================
    Functions :
        - import_daily_jsons : read daily json
        - write_filtering_jsons
============================================================================"""


def import_daily_jsons(path_source):
    """
        Summary:
            Import a panel of article from robot group (g4) according to the
            server structure :
                [date] / path_source / newspaper / article
            where "date" corresponds to the most recent repository.
        In:
            - path_source : a string which corresponds to the localisation
                 of robot group (g4)
        Out:
            - articles : a dict of articles
    """
    # Initialisation
    articles = {}
    # Get today directory
    today = datetime.now().strftime('%Y-%m-%d')
    dates_ls = listdir(path_source)
    if today in dates_ls:
        path_source += ('/' + today)
    else:
        path_source += ('/' + dates_ls[-1])
    newspaper_ls = listdir(path_source)
    # Loop: For each inewspaper
    for inewspaper in newspaper_ls:
        # management of hidden repositories: required on mac (.ds_store)
        if not inewspaper.startswith('.'):
            xdirpaper = path_source + '/' + inewspaper
            files_ls = listdir(xdirpaper)
            # progress bar for each newspaper repository
            with tqdm(desc=inewspaper, total=len(files_ls)) as fbar:
                # Loop: For each file
                for ifile in files_ls:
                    if not ifile.startswith('.'):
                        iname = findall('^(.*?)_robot.json', ifile)[0]
                        # Import Json
                        with open(xdirpaper + '/' + ifile, 'r',
                                  encoding='utf-8') as dict_robot:
                            articles[iname] = json.load(dict_robot)
                    fbar.update()
                    continue
                # End newspaper repository
        continue
    # End all newspapers
    return articles