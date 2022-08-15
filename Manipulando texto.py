frase = 'Curso em Vídeo Python'
print(len(frase))  # Ver o tamanho da frase (len)
print(len(frase.strip()))  # Ver o tamanho da frase Removendo os espaços (strip)
print(frase.replace('Python', 'Android'))  # Trocar palavra Python por Android
print('Curso' in frase)  # Verificar se a palavra curso esta dentro da frase
frase = frase.replace('Python', 'Android')  # Trocar Palavra Python por Android so que pedindo pra salvar
print(frase)
print(frase.split())  # Divide a frase em uma lista
dividido = frase.split()
print(dividido[0])  # Divide o primeiro item da lista
