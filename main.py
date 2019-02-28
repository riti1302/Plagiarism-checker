import os
from difflib import SequenceMatcher
import multiprocessing
import PyPDF2
from fuzzywuzzy import fuzz 
from tqdm import tqdm 

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
	except:
		pass
	return flag

def thread1(patch1, returns1):
	for folder in tqdm(patch1):
		folder = os.path.join(path,folder)
		flag = check_ratio(folder)
	returns1[0] = flag

def thread2(patch2, returns2):
	for folder in tqdm(patch2):
		folder = os.path.join(path,folder)
		flag = check_ratio(folder)
	returns2[0] = flag

def thread3(patch3, returns3):
	for folder in tqdm(patch3):
		folder = os.path.join(path,folder)
		flag = check_ratio(folder)
	returns3[0] = flag

def thread4(patch4, returns4):
	for folder in tqdm(patch4):
		folder = os.path.join(path,folder)
		flag = check_ratio(folder)
	returns4[0] = flag

if __name__ == '__main__':
	File = 'sample.pdf'
	path = 'dataset/'
	global flag
	flag = 0

	listOfFile = os.listdir(path)
	numberOfFiles = len(os.listdir(path))
	numberOfThreads = 4

	partition = [int(numberOfFiles*i/numberOfThreads) for i in range(0,numberOfThreads+1)]
	manager = multiprocessing.Manager()
	#print(partition)

	patch = []
	patches = []
	for i in partition:
		if i != 0:
			patch = listOfFile[j:i]
			patches.append(patch)
		j = i
	
	returns1 = manager.dict()
	returns2 = manager.dict()
	returns3 = manager.dict()
	returns4 = manager.dict()
	
	p1 = multiprocessing.Process(target=thread1, args=(patches[0:1][0], returns1)) 
	p2 = multiprocessing.Process(target=thread2, args=(patches[1:2][0], returns2)) 
	p3 = multiprocessing.Process(target=thread3, args=(patches[2:3][0], returns3)) 
	p4 = multiprocessing.Process(target=thread4, args=(patches[3:4][0], returns4)) 
	process = [p1, p2, p3, p4]
	for p in process:
		p.start()
	for p in process:
		p.join()

	if returns1[0] == 0 and returns2[0] == 0 and returns3[0] == 0 and returns4[0] == 0:
		print("Bravo! Original thesis")
	else:
		print("Copied work")

