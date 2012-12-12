#!/usr/bin/env python3

####################################
##			          ##
##  LICENCE GPL V3                ##
####################################

# CONTRIBUTEUR :
# - TENISTU

# BASE DE PYTHON
# 1 - SYNTAXE DES BOUCLES ET DES TESTES À TRAVERS L'ÉCRITURE

# librarie
import random

#fonction qui affiche pile sur la sortie standart (terminal)
def affichepile():
	#print permet d'affihcer ce qui est entre les parenthèses
	print("pile")


#fonction qui affiche notre entrée en sortie
def afficheentree(mots):
	#on affiche le contenu de la variable mots
	print("le mot affiché est : ",mots," et c'est bien")

#fonction qui sort un pile ou un face
def pileface():
	#on crée une variable aléa
	# on a tiré un nombre uniforme entre O et 1 avec la fonction random.random()
	alea = random.random()
	#On affiche notre nombre avec print
	print("Notre nombre aléatoire est : ",alea)

	# on test notre nombre, par convention s'il est supérieur à 0.5 alors face
	if alea > 0.5:
		print("face")
	else:
		print("pile")

#fonction qui affiche un certains nombre de parties pile ou face
def pilefacepartie(nbpartie):
	# nbpartie est le nombre de parties qu'on souhaite joué
	print("le nombre de parties est : ", nbpartie)
	
	#On crée simplement une variable i qui fera office de compteur
	#On part de 0 et veut aller jusqu'au nombre désiré

	i = 0

	while( i < nbpartie ):
		print("===================== Partie numéro : " , (i+1), " =====================")
		pileface()
		i = i + 1

# Main - on appelle nos fonctions
affichepile()
afficheentree("Poulet")
pilefacepartie(5)








