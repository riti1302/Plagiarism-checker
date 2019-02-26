import os
from difflib import SequenceMatcher
import multiprocessing
import PyPDF2


def read_pdf(file):
	pdfFileObject = open(file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
	count = pdfReader.numPages
	string = ""
	for i in range(count):
	    page = pdfReader.getPage(i)
	    content = page.extractText()
	    string += content
	return string

def thread1(patch1, return1):
	flag = 0
	for file in patch1:
		file = os.path.join(path, file)
		check_data = read_pdf(File)
		database_data = read_pdf(file)
		similarity_ratio = SequenceMatcher(None, check_data, database_data).ratio()
		#print(similarity_ratio)

		if similarity_ratio > 0.1:               #To increase the string matching efficiency, decrease the similarity ratio 
			print("Copied thesis from {}".format(file))
			flag = 1
		return1[flag] = flag

def thread2(patch2, return2):
	flag = 0
	for file in patch2:
		file = os.path.join(path, file)
		check_data = read_pdf(File)
		database_data = read_pdf(file)
		similarity_ratio = SequenceMatcher(None, check_data, database_data).ratio()
		#print(similarity_ratio)

		if similarity_ratio > 0.1:               #To increase the string matching efficiency, decrease the similarity ratio 
			print("Copied thesis from {}".format(file))
			flag = 1
		return2[flag] = flag

if __name__ == '__main__':
	File = 'Primjer_esej.pdf'
	path = 'Database/'

	listOfFile = os.listdir(path)
	numberOfFiles = len(os.listdir(path))
	p1 = int(numberOfFiles/2)
	patch1 = listOfFile[0:p1]
	patch2 = listOfFile[p1:numberOfFiles]
	
	manager = multiprocessing.Manager()
	return1 = manager.dict()
	return2 = manager.dict()

	p1 = multiprocessing.Process(target=thread1, args=(patch1, return1)) 
	p2 = multiprocessing.Process(target=thread2, args=(patch2, return2)) 

	p1.start()
	p2.start()

	p1.join()
	p2.join()

	if return1 == 0 and return2 == 0:
		print("Bravo! Original thesis")


