#!  /usr/bin/env python
# -*- coding: utf-8 -*-

#	du 11 février 2019, 19:26:19 (UTC+0100)
# 	génération de la sem suiv. à partir de rien

#	/home/yves/2011/dev/Python/outils/pyNewMap/
from newMap import insDir

def insDu(c):
	''' insère date '''
	#	grep -ni insdir /media/home/yves/2011/dev/Python/outils/pyNewMap/newMap.py
	#	434:def insDir(c):

	from semaineSuivante import lundiProchain

	du = str(lundiProchain())
	du = du.split('-')

	q = du[2]
	numMois = int(du[1])

	m = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'decembre'][numMois - 1]

	if True:
		print 'insDu(c) : m = {}'.format(m)
	y = du[0]	# year
	assert 0, (q, m, y)

def aBovo():
	''' '''
	from bugGicl import dirCartes, numSemCour
	n = numSemCour() + 1

	from insWeek import annee2chiffres
	an = annee2chiffres()
	nomc = 'Sem{:02d}{}'.format(n, an)

	import newMap

	c = newMap.main(nombase = nomc, dater = False, leDir = '.', over = True)
	insDu(c)
	insDir(c)
	assert 0, c

if __name__ == '__main__':
	aBovo()
