
import sys

def randomize_cards():
    """randomizes a specific number of cards to append to a player's card set
    
    HOW TO USE:
    
    python card_randomizer.py [number] [player]
    python card_randomizer.py 5 treepuncher_27
    """

    # estos dos son parámetros que se le pasan al fichero por consola de python
    number = int(sys.argv[1]) # número de cartas que se quieren anexar al card set
    player = sys.argv[2] # jugador al que se le quieren anexar esas cartas
    card_set_route = (f"../card_sets/{player}.txt") # ruta donde se encuentra el fichero de texto con las cartas
    #TODO: [CAMBIO] de momento se está jugando con txt files. lo ideal es cambiar todo a json para que cuadre con la info que está devolviendo la api

    cards = list(range(number)) #TODO por el momento lo que representa a cada carta es un número es un número de esta lista. hay que cambiarlos por nombres de cartas randomizadas.

    with open(card_set_route, 'a') as f: # the new cards are appended to the already existing ones
        for card in cards:
            f.write("%s\n" % card)

    return "CARDS APPENDED CORRECTLY"

if __name__ == "__main__":
    print(randomize_cards()) # the print function outputs the string in the return
