# %%

txt = "Meu novo arquivo!"

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, mode="w") as open_file:
    open_file.write(txt)

# %%

txt = "Quero adiconar mais texto ao meu arquivo!\n"

nome_arquivo = "historia_02.txt"

with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)

