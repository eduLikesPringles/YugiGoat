""" 
este fichero contiene las constantes y las llamadas a los ficheros de interés
cada fichero tiene una clase o clases que ejecuta una o varias funciones
según lo que se quiera hacer, hay que comentar o descomentar la línea que invoca a la clase de interés
y finalmente en /src correr python main.py
VOILÁ!

el fichero hello.py con su clase Person es un ejemplo de uso

"""

import requests
import json
import os
import random
import sys

from hello import Person
from card_json_fetcher import card_json_fetcher

p1 = Person("John", 36)
cjf = card_json_fetcher()

""" print(p1.name)
print(p1.age)
p1.say_hi() """