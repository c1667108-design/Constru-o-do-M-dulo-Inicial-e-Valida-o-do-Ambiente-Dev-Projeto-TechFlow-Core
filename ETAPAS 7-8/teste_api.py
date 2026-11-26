from api import consultar_cep

cep = input("Digite um CEP: ")

dados = consultar_cep(cep)

print("Cidade:", dados["localidade"])
print("Estado:", dados["uf"])
print("Bairro:", dados["bairro"])