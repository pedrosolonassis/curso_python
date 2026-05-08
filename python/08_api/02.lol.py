# %%
import requests
import pandas as pd

api_key = "RGAPI-67432002-7f89-4650-95dd-177daa99a94f"
url = "https://br1.api.riotgames.com/lol/platform/v3/champion-rotations"
headers = {"X-Riot-Token": api_key}

requisicao = requests.get(url, headers=headers)
dados = requisicao.json()

if requisicao.status_code == 200:
    df = pd.DataFrame(dados['freeChampionIds'], columns=['ID_Campeao'])
    print("Sucesso! Aqui estão os IDs da rotação:")
    print(df.head())
else:
    print(f"Erro {requisicao.status_code}: Algo deu errado!")
    print("Resposta do servidor:", dados)
