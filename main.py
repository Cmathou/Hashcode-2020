import random
import math
from Utils import *


inFile = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
outFile = ["a_out.txt", "b_out.txt", "c_out.txt", "d_out.txt", "e_out.txt", "f_out.txt"]

continuous = True

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


def process(bookNumber, BookScores, libNumber, libList, BooksPerDayList, daysNumber, nbJoursSignupList):
	bookEffValue = BookScores
	bookRepartition = [0] * bookNumber

	for i in range(libNumber):
		for element in libList[i]:
			bookRepartition[element] += 1
	for i in range(len(bookEffValue)):
		if (bookRepartition[i] != 0):
			bookEffValue[i] /= bookRepartition[i]

	libScore = [0] * libNumber
	for i in range(libNumber):
		print(float(i)/libNumber * 100.0)
		libScore[i] = np.median([bookEffValue[j] for j in libList[i]])**2 * BooksPerDayList[i] * min(daysNumber - nbJoursSignupList[i], float(len(libList[i]))/BooksPerDayList[i]) / np.mean([bookEffValue[j] for j in libList[i]])
	
	libResult = libList
	for i in range(libNumber):
		libResult[i] = [x for _,x in sorted(zip(bookEffValue, libResult[i]), reverse=True)]
	return libResult, [x for _,x in sorted(zip(libScore, list(range(libNumber))), reverse=True)]

def main(fileNbr):
	bookNumber, libNumber, daysNumber, libList, nbJoursSignupList, BooksPerDayList, BookScores = lecture(fileNbr)
	bookList, order = process(bookNumber, BookScores, libNumber, libList, BooksPerDayList, daysNumber, nbJoursSignupList)
	save(fileNbr, order, bookList)


#ligne1: numberOfLib A, 
#rest: libDescription * A
#	l1: libID Y, numberOfBooksScaned K
#	l2: books (in the order they are sent)
def save(fileNbr, libSign, libBook):
	file = open(outFile[fileNbr], "w")
	file.write(str(len(libSign)) + "\n")
	for i in range(len(libSign)):
		file.write(arrayToOut([libSign[i], len(libBook[libSign[i]])]))
		file.write(arrayToOut(libBook[libSign[i]]))
	file.close()

def arrayToOut(array):
	ret = ""
	for i in range(len(array) - 1):
		ret += str(array[i]) + " "
	if (type(array) == int):
		ret += str(array) + "\n"
	else:
		ret += str(array[-1]) + "\n"
	return ret

if (__name__ == "__main__"):
	main(4)
	"""
	for i in range(len(inFile)):
		print(inFile[i])
		main(i)"""
