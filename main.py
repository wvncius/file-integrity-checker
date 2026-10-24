import hashlib

def calcular_hash_texto(texto):

	#converter texto para bytes
	dados = texto.encode("utf-8")
	return hashlib.sha256(dados).hexdigest()

def calcular_hash_arquivo(caminho_arquivo):
	#ler arquivo em modo binário
	with open(caminho_arquivo, "rb") as arquivo:
		dados = arquivo.read()
		return hashlib.sha256(dados).hexdigest()
	
resultado = calcular_hash_arquivo("exemplo.txt")
print(resultado)