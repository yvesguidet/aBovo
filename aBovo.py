#!  /usr/bin/env python
# -*- coding: utf-8 -*-

#	lundi 11 février 2019, 19:26:19 (UTC+0100)
# 	génération de la sem suiv. à partir de rien

#	/home/yves/2011/dev/Python/outils/pyNewMap/
from newMap import insDir

def aBovo():
	''' '''
	from bugGicl import dirCartes, numSemCour
	n = numSemCour() + 1

	from insWeek import annee2chiffres
	an = annee2chiffres()
	nomc = 'Sem{:02d}{}'.format(n, an)

	import newMap
	
	c = newMap.main(nombase = nomc, dater = False, leDir = '.', over = True)
	insDir(c)
	assert 0, c

if __name__ == '__main__':
	aBovo()
