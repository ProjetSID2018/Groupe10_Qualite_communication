Les tests sont effectué sur phpMyAdmin.
Il y a 7 procédures à tester.
Il y a 5 triggers à tester.
Il y a 1 fonction à tester.

* Filtrage : 
Test des pprocédures:
	- Test de particle:
La prcedure prend en entree une date de publication et un nom de journal et nous rend l'id ou à été inéré l'article dans la table

La procedure insere deux resultat: le nom du journal dans la table journal et la date de publication et un id 
de l'article dans la table article.
La date est au format YYYY-MM-DD. sinon erreur. 

TEST OK

La procédure marche quelque soit la date de l'article mis en entre.
	- Test de pauthor:
la procedure prend en entre l'id d'un article et le nom d'un auteur, vérifie si le nom de l'auteur est dans la base,
si oui il recupere l'id de l'auteur et l'insere dans la table realize avec l'id de l'article. 
Si il ne le trouve pas, il il le crée puis l'insert.

TEST OK

	- Test de pposotion_word
insert si le mot n'existe pas, update sinon. 2 tests à faire dessus : 
Un pour voir si les mots ont été crées, un autre pour voir s'il ont été update.
Bien tester que la fonction de filtrage pour database rend bien les bon parametres (ex manger mange <- le mange faire gaff)


