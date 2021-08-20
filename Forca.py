import random;
from datetime import date;
from time import sleep;

denovo = 'S';
possiveis = ['Volibear','Kratos','Shadow','Pac-Man','Scorpion'];
word = random.choice(possiveis);
wordp = word.strip().upper(); #PALAVRA CHAVE
wordpl = list(wordp)
misterio = '';
result = None;
i = 0;
tries = 0;

def draw(tries):
    if tries == 0:
        return'\n\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========';
    if tries == 1:
        return'\n\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========';
    elif tries == 2:
        return'\n\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========';
    elif tries == 3:
        return'\n\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========';
    elif tries == 4:
        return'\n\n  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========';
    elif tries == 5:
        return'\n\n  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========';
    else:
        return'\n\n  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n=========';

while denovo.upper() == 'S' and tries <=6:
   
    for c in (wordp):
        misterio += '_';
    result = list(misterio);
    
    print('A palavra é: '+' '.join(list(misterio)));
    print('=-'*20);
    
    while ('_' in result) and tries < 7:
            letra = input('[{}x♥] PALPITE: '.format(6 - tries)).upper();
            print('')
        
            if letra.upper() in wordp:
                if letra =='':
                    print('Digite uma letra!')
                elif letra.upper() in result:
                    print('Letra ja usada!')
                else:
                    print('Bom Palpite');
            else:
                tries +=1;
                print('Tente outro!');
                print(draw(tries));
        
            while i < len(wordpl):
                if wordpl[i] == letra:
                    result[i] = wordpl[i];
                i += 1;
            i = 0;
        
            print(' '.join(result))
            
            print('-'*15)
            print('')
    
    print('=-'*20);
    
    print('FIM DE JOGO');

    denovo = input('Jogar novamente?(S/N) ');
   
   #REDEFININDO AS VARIAVEIS
    word = random.choice(possiveis);
    wordp = word.strip().upper(); #PALAVRA CHAVE
    wordpl = list(wordp)
    misterio = '';
    result = None;
    tries = 0;

    print('\n\n');
input();
