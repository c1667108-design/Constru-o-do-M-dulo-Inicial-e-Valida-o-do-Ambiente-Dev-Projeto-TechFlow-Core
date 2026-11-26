import urllib.request
import json


def consultar_cep(cep):
    """Consulta um CEP utilizando a API ViaCEP."""

    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = urllib.request.urlopen(url)
    dados = json.loads(resposta.read().decode("utf-8"))

    return dados