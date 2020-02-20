import random
import numpy
import math

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
			nBooks, signupTime, booksPerDay = [int(i) for j in i.split()]
			BooksPerDayList.append(booksPerDay)
			nbJoursSignupList.append(signupTime)
		else:
			l1 = True
			libList.append([int(i) for j in i.split()])

	return bookNumber, libNumber, daysNumber, libList, nbJoursSignupList, BooksPerDayList




def main(fileNbr):
	
	lecture(fileNbr)



#ligne1: numberOfLib A, 
#rest: libDescription * A
#	l1: libID Y, numberOfBooksScaned K
#	l2: books (in the order they are sent)
def save(fileNbr, libSign, libBook):
	file = open(outFile[fileNbr], "w")
	file.writelines(len(libSign))
	for i in range(len(libSign)):
		file.writelines(libSign[i])
		file.writelines(libBook[i])
	file.close()

if (__name__ == "__main__"):
	for i in range(len(inFile)):
		main(i)
