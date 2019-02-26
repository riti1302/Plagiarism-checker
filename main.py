import os
from difflib import SequenceMatcher

File = 'coverLetter.txt'
path = 'database/'
flag = 0

for file in os.listdir(path):
	checkfile = os.path.join(path, file)
	with open (File) as file_1, open(checkfile) as file_2:
		file1_data = file_1.read()
		file2_data = file_2.read()
		similarity_ratio = SequenceMatcher(None, file1_data, file2_data).ratio()
		print(similarity_ratio)

	if similarity_ratio > 0.1:
		print("Copied thesis from {}".format(file))
		flag = 1

if flag == 0:
	print("Original thesis")
