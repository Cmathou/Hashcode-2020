#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:00:07 2020

"""

import numpy as np

def sortBooks(Scores, listBooks):
	listScores = []
	for i in range(len(listBooks)):
		listScores.append(Scores[i])
	ponderee = [x for _,x in sorted(zip(listScores, listBooks))]

	return ponderee

def CalcLibScore(listBooks, listDays, listNbBooks, Scores, libNumber):
    
    LibScore = []
    BooksToSend = []
    
    for lib in range(libNumber):
        #Sort the books by score (the best at first)
        sortedBooks = sortBooks(Scores, listBooks[lib])
        
        BooksToSend.append(sortedBooks)
        
        #Calcul du score de la librairy compte tenu de ses meilleurs bouquins et jours
        LibScore.append(0)
        
        for book in sortedBooks :
            LibScore[lib] += Scores[book]
        
        LibScore[lib] /= listDays[lib]
    
    return LibScore, BooksToSend


def ChooseBestLib(LibScore):
    
    return np.argmax(LibScore)

def DelSuppr(listBooks, BookToDel):
    
    for book in BookToDel :
        for lib in range(len(listBooks)) :
            if book in listBooks[lib]:
                listBooks[lib].remove(book)
                
    return listBooks
                





#Order :
"""
CalcLibScore
Choose best score
Envoir Books
Del books dans toutes les list books

recommence


"""
        
        
