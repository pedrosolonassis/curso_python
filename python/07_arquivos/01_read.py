# %%
nome_arquivo = "historia.txt"

# Abrindo o arquivo em formato de leitura
open_file = open(nome_arquivo)

print(open_file)

# Lê os dados do arquivo
conteudo = open_file.read()
print(conteudo)

# Fechando o arquivo 
open_file.close()

# Uma melhor maneira de abrir um arquivo
# %%

nome_arquivo = "historia.txt"
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
    
print(conteudo)