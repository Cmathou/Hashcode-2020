import random
import numpy
import math

inFile = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
outFile = ["a_out.txt", "b_out.txt", "c_out.txt", "d_out.txt", "e_out.txt", "f_out.txt"]

def main(fileNbr):
	data = open("problem/" + inFile[fileNbr], "r")
	lines = data.readlines()

	#ligne1 bookNumber B, libNumber L, daysNumber D
	#ligne2 BooksScore * B
	#rest: L * 2lignes
	#	l1: numberOfBooks N, signupTime T, booksPerDay M
	#	l2: BookID * N


	[bookNumber, libNumber, daysNumber] = [int(i) for i in lines[0].split()]
	BookScores = [int(i) for i in lines[1].split()]


	for i in lines[2:]:



		theMagicReturn = ""



	testFile = open(outFile[fileNbr], "w")

	testFile.write(theMagicReturn)
	#ligne1: numberOfLib A, 
	#rest: libDescription * A
	#	l1: libID Y, numberOfBooksScaned K
	#	l2: books (in the order they are sent)


	testFile.close()
	data.close()

if (__name__ == "__main__"):
	for i in range(len(inFile)):
		main(i)