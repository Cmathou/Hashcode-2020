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
def SortIdeeFaramineuse(Libs, Scores):

    Scores, Libs = [y,x for y,x in sorted(zip(Scores, Libs))]

    return Libs, Scores

def CreaListes(listLibs, listDays, listNbBooks, Scores, libNumber, jourPasse, jourTot):
    listeLibsSortedBySignupDays = [[] for i in range(max(listDays))]
    listeScoresSortedBySignupDays = [[] for i in range(max(listDays))]

    LibScore, BookToSend = CalcLibScore(listLibs, listDays, listNbBooks, Scores, libNumber, jourPasse, jourTot )

    for libIndex in range(len(listLibs)):
        listeLibsSortedBySignupDays[libIndex].append(listLibs[libIndex])
        listeScoresSortedBySignupDays[libIndex].append(LibScore[libIndex])

    for i in range(len(listeLibsSortedBySignupDays)):
        listeLibsSortedBySignupDays[i], listeScoresSortedBySignupDays[i] = SortIdeeFaramineuse(listeLibsSortedBySignupDays[i], listeScoresSortedBySignupDays[i])

    return listeLibsSortedBySignupDays, listeScoresSortedBySignupDays

def SortIdeeFaramineuse(Libs, Scores):

    Scores, Libs = [y,x for y,x in sorted(zip(Scores, Libs))]

    return Libs, Scores

def CreaListes(listLibs, listDays, listNbBooks, Scores, libNumber, jourPasse, jourTot):
    listeLibsSortedBySignupDays = [[] for i in range(max(listDays))]
    listeScoresSortedBySignupDays = [[] for i in range(max(listDays))]

    LibScore, BookToSend = CalcLibScore(listLibs, listDays, listNbBooks, Scores, libNumber, jourPasse, jourTot )

    for libIndex in range(len(listLibs)):
        listeLibsSortedBySignupDays[libIndex].append(listLibs[libIndex])
        listeScoresSortedBySignupDays[libIndex].append(LibScore[libIndex])

    for i in range(len(listeLibsSortedBySignupDays)):
        listeLibsSortedBySignupDays[i], listeScoresSortedBySignupDays[i] = SortIdeeFaramineuse(listeLibsSortedBySignupDays[i], listeScoresSortedBySignupDays[i])

    return listeLibsSortedBySignupDays, listeScoresSortedBySignupDays

def CalcLibScore(listBooks, listDays, listNbBooks, Scores, libNumber, jourPasse, jourTot):
    
    LibScore = []
    BooksToSend = []
    
    for lib in range(libNumber):
        #Sort the books by score (the best at first)
        sortedBooks = sortBooks(Scores, listBooks[lib])
        BooksToSend.append(sortedBooks[:min(len(sortedBooks), jourTot-jourPasse-listDays[lib])])
        
        #Calcul du score de la librairy compte tenu de ses meilleurs bouquins et jours
        LibScore.append(0)
        
        for book in sortedBooks[:min(len(sortedBooks), jourTot-jourPasse-listDays[lib])] :
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
        
        
