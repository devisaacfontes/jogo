import random

def escolher_palavra():
    palavras = ["python", "programação", "desenvolvimento", "jogo", "computador", "inteligencia", "algoritmo", "variavel", "função", "classe"]
    return random.choice(palavras)

def exibir_forca(tentativas):
    estagios = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           
           
           
           
           
        """
    ]
    return estagios[tentativas]

print("Bem-vindo ao Jogo da Forca!")

palavra= escolher_palavra()
Letras_acertadas = []
Letras_erradas = []
tentativas = 6
while tentativas > 0:
    print(exibir_forca(tentativas))
    print("palavra:", " ".join([Letra if Letra in Letras_acertadas else "_" for Letra in palavra]))
    print("Letras erradas:", " ".join(Letras_erradas if Letras_erradas else "Nenhuma"))
    Letra = input("Digite uma Letra: ").lower()
    if Letra in Letras_acertadas or Letra in Letras_erradas:
        print("você já tentou essa Letra.")
    elif Letra in palavra:
        Letras_acertadas.append(Letra)
        if all(Letra in Letras_acertadas for Letra in palavra):
            print("parabens! Voce acertou a palavra:", palavra)
            break
    else:
        Letras_erradas.append(Letra)
        tentativas -= 1
        if tentativas == 0:
            print(exibir_forca(tentativas))
            print("voce perdeu! A palavra era:", palavra)
            break
print("obrigado por jogar!")

