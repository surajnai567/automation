import os
import re

folder_location = "C:\\Users\\ani\\Desktop\\html\\in.codingninjas.app_source_from_JADX"
text_to_search = re.compile('LocalMediaDrmCallback')
log_file = open("log.txt", 'wt', encoding='UTF-8')

for root, dir, files in os.walk(folder_location):
	for file in files:
		line_number = 1
		with open(os.path.join(root, file), encoding='UTF-8', errors='ignore') as f:
			for line in f:
				match = text_to_search.search(line)
				if match is not None:
					message = f'folder:{root}, filename:{file}, line_number:{line_number}'
					print(message)
					log_file.write(message)
					log_file.write("\n")

				line_number += 1

log_file.close()
