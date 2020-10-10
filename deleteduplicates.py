import os


def get_all_file(file_location):
	files = []
	for file in os.listdir(file_location):
		if os.path.isfile(os.path.join(file_location, file)):
			files.append(file)
	return files


