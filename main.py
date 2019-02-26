import os
from difflib import SequenceMatcher
import multiprocessing

File = 'coverLetter.txt'
path = 'database/'
flag = 0
listOfFile = os.listdir(path)
#print(listOfFile)
numberOfFiles = len(os.listdir(path))
p1 = int(numberOfFiles/2)
print("p1 ", p1)
patch1 = listOfFile[0:p1]
patch2 = listOfFile[p1:numberOfFiles]

def thread1(patch1):
	for file in patch1:
		file = os.path.join(path, file)
		with open (File) as file_1, open(file) as file_2:
			check_data = file_1.read()
			database_data = file_2.read()
			similarity_ratio = SequenceMatcher(None, check_data, database_data).ratio()
			print(similarity_ratio)

		if similarity_ratio > 0.1:               #To increase the string matching efficiency, decrease the similarity ratio 
			print("Copied thesis from {}".format(file))
			flag = 1

def thread2(patch2):
	for file in patch2:
		file = os.path.join(path, file)
		with open (File) as file_1, open(file) as file_2:
			check_data = file_1.read()
			database_data = file_2.read()
			similarity_ratio = SequenceMatcher(None, check_data, database_data).ratio()
			print(similarity_ratio)

		if similarity_ratio > 0.1:               #To increase the string matching efficiency, decrease the similarity ratio 
			print("Copied thesis from {}".format(file))
			flag = 1

p1 = multiprocessing.Process(target=thread1, args=(patch1, )) 
p2 = multiprocessing.Process(target=thread2, args=(patch2, )) 

p1.start()
p2.start()

p1.join()
p2.join()

#if flag == 0:
#	print("Original thesis")
