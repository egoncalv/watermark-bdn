import os
from PIL import Image

sq_fit_size = 1080
logo_file = input("Arquivo Marca D'água: ")
img_folder = input("Diretório com imagens: ")

if not (os.path.exists(img_folder)):
	print("Diretório de Imagens não existe")

if not (os.path.isfile(logo_file)):
	print("Logo não existe")

logoIm = Image.open(logo_file)
logoWidth, logoHeight = logoIm.size

os.makedirs("Imagens com Logo", exist_ok = True)

for filename in os.listdir(img_folder):
	if not (filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png")) or filename == logo_file:
		continue
	img = Image.open(os.path.join(img_folder, filename))
	width, height = img.size
	print("Adicionando Marca D'água à", filename)
	img.paste(logoIm, (width - logoWidth, 0), logoIm)
	img.save(os.path.join("Imagens com Logo", filename))

print("Pronto!")
