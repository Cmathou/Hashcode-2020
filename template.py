import random
import numpy
import math

def main():
	data = open("input.txt", "r")
	lines = data.readlines()

	#ligne1 bookNumber B, libNumber L, daysNumber D
	#ligne2 BooksScore * B
	#rest: L * 2lignes
	#	l1: numberOfBooks N, signupTime T, booksPerDay M
	#	l2: BookID * N


	bookNumber, libNumber, daysNumber = int(i) for i in lines[0].split()
	BookScores = [int(i) for i in lines[1].split()]


	for i in lines[2:]:



		theMagicReturn = ""



	testFile = open("output.txt", "w")

	testFile.write(theMagicReturn)
	#ligne1: numberOfLib A, 
	#rest: libDescription * A
	#	l1: libID Y, numberOfBooksScaned K
	#	l2: books (in the order they are sent)


	testFile.close()
	data.close()

if (__name__ == "__main__"):
	main()