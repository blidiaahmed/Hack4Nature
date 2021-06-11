import os

def save_image(filename, image):
	with open(filename, "wb") as fp:
		for chunk in image:
			fp.write(chunk)
	return True

def delete_image(filename):
	os.remove(filename)
	return True