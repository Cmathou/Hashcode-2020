#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:00:07 2020

@author: toinou
"""
def sortBooks(Scores, listBooks):
	listScores = []
	for i in range(len(listBooks)):
		listScores.append(Scores[i])
	ponderee = [x for _,x in sorted(zip(listScores, listBooks))]

	return ponderee

def Recover(listBooks, listDays, listNbBooks, Scores, libNumber):
    
    LibScore = []
    
    for lib in range(libNumber):
        #Sort the books by score (the best at first)
        sortedBooks = sortBooks(Scores, listBooks[lib])
        
        #Recover the best books that we ca send
        getBooks = sortedBooks[:listNbBooks[lib]]
        
        LibScore.append(0)
        
        for book in getBooks :
            LibScore[lib] += Scores[book]
        
        LibScore /= listDays[lib]
    
    
        
        
