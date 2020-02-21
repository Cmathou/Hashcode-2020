#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:00:07 2020

"""
import math
import numpy as np

def sortBooks(Scores, listBooks):
    listScores = []
    for i in listBooks:#range(len(listBooks)):
    	listScores.append(Scores[i])
    # listScores = [Scores[i] for i in listBooks]
    ponderee = [x for _,x in sorted(zip(listScores, listBooks))]

    return ponderee

def SortIdeeFaramineuse(Libs, Scores):

    Libs = [x for _,x in sorted(zip(Scores, Libs))]
    Scores = sorted(Scores)

    return Libs, Scores

def CreaListes(listLibs, listDays, listNbBooks, Scores, libNumber, jourPasse, jourTot):
    listeLibsSortedBySignupDays = [[] for i in range(max(listDays)+1)]
    listeScoresSortedBySignupDays = [[] for i in range(max(listDays)+1)]

    LibScore, BookToSend = CalcLibScore(listLibs, listDays, listNbBooks, Scores, libNumber, jourPasse, jourTot )

    for libIndex in range(len(listLibs)):
        listeLibsSortedBySignupDays[listDays[libIndex]].append(libIndex)
        listeScoresSortedBySignupDays[listDays[libIndex]].append(LibScore[libIndex])

    for i in range(len(listeLibsSortedBySignupDays)):
        listeLibsSortedBySignupDays[i], listeScoresSortedBySignupDays[i] = SortIdeeFaramineuse(listeLibsSortedBySignupDays[i], listeScoresSortedBySignupDays[i])

    return listeLibsSortedBySignupDays, listeScoresSortedBySignupDays, BookToSend

def CalcLibScore(listBooks, listDays, listNbBooks, Scores, libNumber, jourPasse, jourTot):
    
    LibScore = []
    BooksToSend = []
    
    for lib in range(libNumber) :

        #Sort the books by score (the best at first)
        sortedBooks = sortBooks(Scores, listBooks[lib])
        slicedList = sortedBooks[:min(len(sortedBooks), (jourTot-jourPasse-listDays[lib]) * listNbBooks[lib])]
        BooksToSend.append(slicedList)
        
        #Calcul du score de la librairy compte tenu de ses meilleurs bouquins et jours
        LibScore.append(0)
        
        for book in slicedList :
            LibScore[lib] += Scores[book]
            
    return LibScore, BooksToSend


def ChooseBestLib(ListScoreSignUpDays):
    
    listBest = []
    
    for sign in ListScoreSignUpDays :
        if len(sign) == 0 :
            listBest.append(-1)
        else :
            listBest.append(sign[0])
    
    return np.argmax(listBest)

def CheckX2(libSignX2, ScoreX2, bookToSendX2,indexBest, listBooks, ScoreBook, listDays, listNbBooks, jourPasse, jourTot):
    
    val = int(math.floor(indexBest/2))

    if (len(ScoreX2[val]) == 0) or (len(bookToSendX2[val]) == 0):
        return False, 0,0
    
    
    libSignX2 = libSignX2[val]
    ScoreX2 = ScoreX2[val][0]
    bookToSendX2 = bookToSendX2[val][0]
    ScoreBest = ScoreX2[indexBest][0]
    
    ScoreFin = ScoreX2
    mylistDays = []
    mylistNbBooks = []
    myBooks = []
    for lib in libSignX2[1:]:
        myBooks.append(listBooks[lib])
        for book in bookToSendX2 :
            if book in myBooks[-1]:
                myBooks[-1].remove(book)
    
        mylistDays.append(listDays[lib])
        mylistNbBooks.append(listNbBooks[lib])
    
    LibScore, BooksToSend = CalcLibScore(myBooks, mylistDays, mylistNbBooks, ScoreBook, len(libSignX2[1:]), jourPasse + listDays[libSignX2[0]], jourTot)
    
    ScoreFin += max(LibScore)
    
    if ScoreFin < ScoreBest:
        return False, 0, 0
    
    index = np.argmax(LibScore)
    
    indexesBest = [libSignX2[0], libSignX2[index]]
    booksUpdated = BooksToSend[index]
    
    return True, indexesBest, booksUpdated

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
        
        
