# Vytvoř hru sibenice podle následujícího popisu. Snaž se projekt rozdělit do funkcí a modulů s hezkými
# jmény, piš testy a dokumentační řetězce, funkční kousky dávej postupně do Gitu.
# • Počítač náhodně zvolí slovo (zatím třeba ze tří možností). Pro jednoduchost používej malá písmena a
# nepoužívej slova, ve kterých se stejné písmeno opakuje dvakrát (třeba čokoláda).
# • Nastav výchozí stav: řetězec s tolika podtržítky, kolik je ve vybraném slově písmen.
# • Nastav počet neúspěšných pokusů na nulu.
# • Každý tah:
# – Zeptej se hráče na písmeno.
# – Pokud je to písmeno ve vybraném slově, zaměň příslušná podtržítka za ono písmeno.
# Bude se hodit řetězcová metoda index a funkce zamen z piškvorek.
# – Pokud dané písmeno není ve vybraném slově, započítej neúspěšný pokus.
# – Vypiš stav (slovo s případnými podtržítky).
# – Pokud už ve slově nejsou podtržítka, pogratuluj hráči a ukonči hru.
# – Podle počtu neúspěšných pokusů vypiš „obrázek”. Obrázky jsou ke stažení na
# http://pyladies.cz/v1/s005-modules/obrazky.txt a můžeš je dát do víceřádkových řetězců
# (s trojitými uvozovkami).
# – Pokud jsi právě vypsala poslední obrázek, hráč prohrál. Dej mu to najevo a ukonči program.

import pictures
from random import randrange

def choose_word():
    "Náhodně se vybere slovo z listu"
    list_of_words = ["aftershock", "background", "trampoline", "cat"]
    return list_of_words[randrange(len(list_of_words))]

def set_stage(word):
    "Nastaví se prázdné pole"
    stage = ['-'] * len(word)
    return stage

def print_stage(stage):
    "Vypíše současné pole"   
    for i in stage:
        print(i, end='')
    print('\n')

def input_letter(stage):
    "Hráč zadá malé písmeno, ověří se, zda je mezi dovolenými znaky, pokud ne, vyzve ho k novéhu zadání"
    # Pouze anglická abeceda a taky ověřím, že má řetězec pouze 1 znak, taky ověří, zda písmeno už nebylo odhaleno
    while True:
        input_letter = input("Please input lowercase letter: ")
       
        if len(input_letter) == 1 and ord(input_letter) in range(97, 123, 1) and not input_letter in stage:
            return input_letter
        else:
            continue

def game_result(stage):
    "Vrátí výsledek hry"
    if '-' in stage:
        return "GAME OVER"
    else:
        return "YOU WON!"
  
def hangman():
    "Samotná hra hangman"
    fails = 0 # počet neúspěšných pokusů se nastaví na nulu
    word = choose_word()
    stage = set_stage(word) # nastaví se slovo
    print_stage(stage) # vytiskne se prázdné pole

    while fails < 9 and '-' in stage: # po 10 neúspěšných pokusech končí hra
        letter = input_letter(stage) # hráč hádá písmeno

        if letter in word: # pokud je písmeno ve slově, změníme pole
           stage[word.index(letter)] = letter
        else:
            fails += 1 # pokud ne, zvýšíme počet neúspěšných pokusů
            print(pictures.list_of_pictures[fails]) # a vytisneme oběšence
       
        print_stage(stage) # vytiskneme stav pole
    print(game_result(stage))
