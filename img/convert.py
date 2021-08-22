import moviepy.editor as mp
import os

files = os.listdir("./")

for file in files:
	if(file.split(".")[1] != "jpg" and file != "convert.py"):
		print(file)
		try:
			os.rename(file,file.split(".")[0]+".jpg")
		except Exception as e:
			print(e)
			continue
		#os.remove(file)

