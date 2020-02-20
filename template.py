import random
import numpy
import math
from Utils import *


inFile = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
outFile = ["a_out.txt", "b_out.txt", "c_out.txt", "d_out.txt", "e_out.txt", "f_out.txt"]

#ligne1 bookNumber B, libNumber L, daysNumber D
#ligne2 BooksScore * B
#rest: L * 2lignes
#	l1: numberOfBooks N, signupTime T, booksPerDay M
#	l2: BookID * N
def lecture(fileNbr):
	data = open("problem/" + inFile[fileNbr], "r")
	lines = data.readlines()
	data.close()


	[bookNumber, libNumber, daysNumber] = [int(i) for i in lines[0].split()]
	BookScores = [int(i) for i in lines[1].split()]

	libList = []
	nbJoursSignupList = []
	BooksPerDayList = []

	l1 = True
	for i in lines[2:]:
		if l1:
			l1 = False
			[nBooks, signupTime, booksPerDay] = [int(j) for j in i.split()]
			BooksPerDayList.append(booksPerDay)
			nbJoursSignupList.append(signupTime)
		else:
			l1 = True
			libList.append([int(j) for j in i.split()])

	return bookNumber, libNumber, daysNumber, libList, nbJoursSignupList, BooksPerDayList, BookScores




def main(fileNbr):
	nbJour = 0
	bookNumber, libNumber, daysNumber, libList, nbJoursSignupList, BooksPerDayList, BookScores = lecture(fileNbr)
	while nbJour < daysNumber :
		LibScore, BookToSend = CalcLibScore(libList, nbJoursSignupList, BooksPerDayList, BookScores, libNumber )
		indexBest = ChooseBestLib(LibScore)
		libList = DelSuppr(libList, BookToSend[indexBest])
		nbJour += nbJoursSignupList[indexBest]
	save(fileNbr, , BookToSend[indexBest])


#ligne1: numberOfLib A, 
#rest: libDescription * A
#	l1: libID Y, numberOfBooksScaned K
#	l2: books (in the order they are sent)
def save(fileNbr, libSign, libBook):
	file = open(outFile[fileNbr], "w")
	file.write(str(len(libSign)) + "\n")
	for i in range(len(libSign)):
		file.write(arrayToOut([libSign[i], len(libBook[i])]))
		file.write(arrayToOut(libBook[i]))
	file.close()

def arrayToOut(array):
	ret = ""
	for i in range(len(array) - 1):
		ret += str(array[i]) + " "
	ret += str(array[len(array) - 1]) + "\n"
	return ret

if (__name__ == "__main__"):
	for i in range(len(inFile)):
		main(i)
