import json
import random
import sys

class card_randomizer:
    def print_random_card():
        with open('../card_sets/goat_cards.json') as json_file:
            info = json.load(json_file)
            print(info['data'][random.randint(0, 1692)]['name']) #TODO: hay que cambiar ese número total de goat cards a pincho
            return info['data'][random.randint(0, 1692)]['name'] # devuelve una carta random como string

    def print_random_cards(self, amount):
        cards = []
        for i in range(amount):
            cards.append(self.print_random_card())
        return cards

    def save_cards(self, amount):
        with open('../card_sets/edu.txt', 'a') as f: # the new cards are appended to the already existing ones
            cards = self.print_random_cards(self, amount)
            for card in cards:
                f.write("%s\n" % card)
    #TODO: implementar la funcionalidad que borra cartas
    #TODO: implementar la funcionalidad que elige a qué archivo se anexan cartas
    #TODO: implementar card history of states
    #TODO: implementar una funcion que al randomizar una carta, guarde un pdf con sus fotikis
    #TODO: mover las llamadas a la clase al main para que sirva ese fichero como pivote

card_randomizer = card_randomizer
card_randomizer.save_cards(card_randomizer, 2)
