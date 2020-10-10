import os
import shutil

root = "c:\\Users\\ani\\Desktop"


img_format = ['jpg', 'jpeg']
video_format = ['mp4', 'mkv']
doc_format = ['pdf', 'txt']
while True:
	files = os.listdir(root)
	for file in files:
		if os.path.isfile(os.path.join(root, file)):
			file_ext = file.split('.')[-1].lower()
			if file_ext in img_format:
				shutil.move(os.path.join(root, file), os.path.join(root, "image", file))

			if file_ext in video_format:
				shutil.move(os.path.join(root, file), os.path.join(root, "video", file))

			if file_ext in doc_format:
				shutil.move(os.path.join(root, file), os.path.join(root, "doc", file))



