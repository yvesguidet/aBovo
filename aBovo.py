#!  /usr/bin/env python
# -*- coding: utf-8 -*-

#	du 11 février 2019, 19:26:19 (UTC+0100)
# 	génération de la sem suiv. à partir de rien

#	/home/yves/2011/dev/Python/outils/pyNewMap/
from newMap import insDir

def insTexte(c, t):
	''' ins. "t" ds "c" '''
	#	grep -ni insdir /media/home/yves/2011/dev/Python/outils/pyNewMap/newMap.py
	#	434:def insDir(c):

	from lxml import etree
	arbre = etree.parse(c)

	ssArbre = arbre.xpath("/map/node")[0]
	nomCarte = ssArbre.get('TEXT')


	if True:
		print u'insDir : ssArbre = {}'.format(ssArbre)
		print u'insDir : type(ssArbre) = {}'.format(type(ssArbre))
		print u'insDir : nomCarte = {}'.format(nomCarte)

	verrue = etree.Element("node")
	verrue.set('TEXT', t)

	ssArbre.append(verrue)

	import sys

	sys.path.append('/home/yves/2011/dev/Python/XCartes/XNextWeek')

	from postTraitCHebdo import sauveCarte

	sauveCarte(arbre, c)

def insDu(c):
	''' insère date '''

	from semaineSuivante import lundiProchain

	du = str(lundiProchain())
	du = du.split('-')

	q = du[2]
	numMois = int(du[1])

	m = ['janvier', 'fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'decembre'][numMois - 1]

	if True:
		print 'insDu(c) : m = {}'.format(m)
	y = du[0]	# year
	t = 'du {} {} {}'.format(q, m, y)

	insTexte(c, t)

def nuage(c):
	''' ajoute le nuage '''
#	<cloud/>
	assert 0, c

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
	nuage(c)
	assert 0, 'terminer'

if __name__ == '__main__':
	aBovo()
