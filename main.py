import random

def escolher_palavra():
    palavras = ['python', 'desenvolvedor', 'copiloto', 'programação', 'teclado']
    return random.choice(palavras)

def mostrar_tabuleiro(palavra, letras_certas, letras_erradas):
    print('\\nJogo da Forca\\n')
    print('Letras erradas:', ' '.join(letras_erradas))
    print('Palavra:', end=' ')
    for letra in palavra:
        print(letra if letra in letras_certas else '_', end=' ')
    print('\\n')

def receber_palpite(palpites_feitos):
    while True:
        palpite = input('Adivinhe uma letra: ').lower()
        if len(palpite) != 1:
            print('Por favor, insira apenas uma letra.')
        elif palpite in palpites_feitos:
            print('Você já tentou essa letra. Escolha outra.')
        elif not palpite.isalpha():
            print('Por favor, insira uma LETRA.')
        else:
            return palpite

def jogar_novamente():
    return input('Quer jogar novamente? (sim ou não) ').lower().startswith('s')

letras_erradas = ''
letras_certas = ''
palavra_secreta = escolher_palavra()
jogo_encerrado = False

while True:
    mostrar_tabuleiro(palavra_secreta, letras_certas, letras_erradas)
    palpite = receber_palpite(letras_erradas + letras_certas)

    if palpite in palavra_secreta:
        letras_certas += palpite

        letras_faltando = sum(1 for letra in palavra_secreta if letra not in letras_certas)
        if letras_faltando == 0:
            print(f'Parabéns! A palavra secreta era "{palavra_secreta}"! Você ganhou!')
            jogo_encerrado = True
    else:
        letras_erradas += palpite

        if len(letras_erradas) == 6:
            mostrar_tabuleiro(palavra_secreta, letras_certas, letras_erradas)
            print(f'Você perdeu! A palavra secreta era "{palavra_secreta}".')
            jogo_encerrado = True

    if jogo_encerrado:
        if jogar_novamente():
            letras_erradas = ''
            letras_certas = ''
            jogo_encerrado = False
            palavra_secreta = escolher_palavra()
        else:
            break
