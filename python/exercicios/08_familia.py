# Faça um programa que verifique se a pessoa pertence à família “calvo”.

nome = input("Digite o nome da pessoa: ").lower()

if 'calvo' in nome.split(' '):
    print(f"{nome.title()} pertence à família calvo.")
else:
    print(f"{nome.title()} não pertence à família calvo.")

# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “careca”.

nome = input("Digite o nome da pessoa: ").lower()

if 'calvo' in nome.split(' '):
    print(f"{nome.title()} pertence à família calvo.")
elif 'careca' in nome.split(' '):
    print(f"{nome.title()} pertence à família careca.")
else:
    print(f"{nome.title()} não pertence à família calvo nem à família careca.")