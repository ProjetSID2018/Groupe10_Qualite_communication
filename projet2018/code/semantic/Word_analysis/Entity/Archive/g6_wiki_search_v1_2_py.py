# Groupe 6 LAFONT Nicolas, QUESNOT Sandy, VAYSSE Robin
# Version 1.2
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wikipedia as wk


def wikipedia_search(named_entity):

    """
    entree : chaine de caractere correspondant a une entite nommee.
    sortie : lien url de la page wikipedia associee a l'entite de type chaine
             de caractere.
    Cette fonction effectue une recherche sur wikipedia et retourne l'url de la
    page la plus optimale pour une entite nommee donnee.
    """

    wk.set_lang("fr")
    try:
        search = wk.search(named_entity)[0].replace(' ', '_')
    except:
        return("La page demandée n'existe pas.")
    url_begin = 'https://fr.wikipedia.org/wiki/'
    return url_begin + search
