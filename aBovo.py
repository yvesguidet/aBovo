#!  /usr/bin/env python
# -*- coding: utf-8 -*-

#	lundi 11 février 2019, 19:26:19 (UTC+0100)
# 	génération de la sem suiv. à partir de rien

def aBovo():
	''' '''
	from bugGicl import dirCartes, numSemCour
	n = numSemCour() + 1

	from insWeek import annee2chiffres
	an = annee2chiffres()
	nomc = 'Sem{:02d}{}'.format(n, an)
	assert 0, nomc

if __name__ == '__main__':
	aBovo()
