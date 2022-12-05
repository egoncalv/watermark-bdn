import os
from PIL import Image
import readline
import cloudinary
import requests
from io import BytesIO
from dotenv import load_dotenv, find_dotenv
import cloudinary.uploader
import cloudinary.api
import json

load_dotenv(find_dotenv())

cloudinary.config(
	cloud_name=os.getenv("cloud_name"),
	api_key=os.getenv("api_key"),
	api_secret=os.getenv("api_secret")
)

config = cloudinary.config(secure=True)


print("\n***************** Adicionar Marca d'água Bola de Neve *****************\n")
print("Credenciais Cloud_Name e Api_Key Cloudinary: ", config.cloud_name, config.api_key, "\n")

readline.parse_and_bind("tab: complete")
sq_fit_size = 1080

while True:
	logo_file = input("\nArquivo Marca D'água: ")
	if not (os.path.isfile(logo_file)):
		print("\nOps! O arquivo fornecido não existe :(\n")
	else:
		break

while True:
	img_folder = input("\nDiretório com imagens: ")
	if not (os.path.exists(img_folder)):
		print("\nOps! Essa pasta não existe :(\n")
	else:
		break

logoIm = Image.open(logo_file)
logoWidth, logoHeight = logoIm.size

os.makedirs("Imagens com Marca D'água", exist_ok = True)

for filename in os.listdir(img_folder):
	if not (filename.endswith(".HEIC") or filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".png")) or filename == logo_file:
		continue
	print("Cortando imagem ", filename.removesuffix(".HEIC"), "...")
	data = cloudinary.uploader.upload(os.path.join(img_folder, filename), public_id = filename.removesuffix(".HEIC"))
	url = "https://res.cloudinary.com/dli60x7wr/image/upload/f_jpg/c_crop,g_auto,h_3000,q_100,w_3000/" + filename
	download = requests.get(url)
	img = Image.open(BytesIO(download.content))
	width, height = img.size
	print("Adicionando Marca D'água à", filename.removesuffix(".HEIC"), "...\n")
	img.paste(logoIm, (width - logoWidth, 0), logoIm)
	img.save(os.path.join("Imagens com Marca D'água", filename.removesuffix(".HEIC") + ".jpeg"))

print("\nPronto! :)\n")
