import os
from difflib import SequenceMatcher
import multiprocessing
import PyPDF2
from fuzzywuzzy import fuzz 
from tqdm import tqdm 

def check_ratio(folder):
	global flag
	try:
		for file in os.listdir(folder):
			file = os.path.join(folder, file)
			check_data = read_pdf(File)
			database_data = read_pdf(file)
			similarity_ratio = fuzz.ratio(check_data, database_data)
			#token_set_ratio = fuzz.token_set_ratio(check_data, database_data)
			#print("{} - {}".format(file,similarity_ratio))
			if similarity_ratio > 50:               #To increase the string matching efficiency, decrease the similarity ratio 
				print("Copied thesis from {}".format(file))
				flag = 1
				break
	except:
		pass
	return flag


def read_pdf(file):
	pdfFileObject = open(file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObject, strict=False)
	count = pdfReader.numPages
	string = ""
	for i in range(count):
	    page = pdfReader.getPage(i)
	    content = page.extractText()
	    string += content
	return string

def thread1(patch1, return1):
	for folder in tqdm(patch1):
		folder = os.path.join(path,folder)
		flag = check_ratio(folder)
		return1[flag] = flag

def thread2(patch2, return2):
	for folder in tqdm(patch2):
		folder = os.path.join(path,folder)
		flag = check_ratio(folder)
		return2[flag] = flag

def thread3(patch3, return3):
	for folder in tqdm(patch3):
		folder = os.path.join(path,folder)
		flag = check_ratio(folder)
		return3[flag] = flag

def thread4(patch4, return4):
	for folder in tqdm(patch4):
		folder = os.path.join(path,folder)
		flag = check_ratio(folder)
		return4[flag] = flag

if __name__ == '__main__':
	File = 'sample.pdf'
	path = 'dataset/'
	global flag
	flag = 0

	listOfFile = os.listdir(path)
	numberOfFiles = len(os.listdir(path))

	partition = [int(numberOfFiles*i/4) for i in range(0,5)]
	manager = multiprocessing.Manager()
	#print(partition)

	patch = []
	patches = []
	for i in partition:
		if i != 0:
			patch = listOfFile[j:i]
			patches.append(patch)
		j = i
		#print(patch)
	
	return1 = manager.dict()
	return2 = manager.dict()
	return3 = manager.dict()
	return4 = manager.dict()

	p1 = multiprocessing.Process(target=thread1, args=(patches[0:1][0], return1)) 
	p2 = multiprocessing.Process(target=thread2, args=(patches[1:2][0], return2)) 
	p3 = multiprocessing.Process(target=thread3, args=(patches[2:3][0], return3)) 
	p4 = multiprocessing.Process(target=thread4, args=(patches[3:4][0], return4)) 

	process = [p1, p2, p3, p4]
	for p in process:
		p.start()
	for p in process:
		p.join()

	#print(return1, return2, return3, return4)

	if return1[0] == 0 and return2[0] == 0 and return3[0] == 0 and return4[0] == 0:
		print("Bravo! Original thesis")
