"""
Cours : Tutoriel Python - Les exceptions en Python
Lien : https://www.youtube.com/watch?v=D7H3-krqACY

Les exceptions : créer sa propre exception
La classe parente 'Exception' dispose d'un nombre indéfini de paramètre. Dans l'exemple ci-dessous, en créant sa propre
exception, on déclare un constructeur disposant de deux attributs d'instance à savoir le message d'erreur et le code
d'erreur trouvé qui seront affichés à partir de la méthode d'instance 'def __str__(self)'

L'avantage de créer sa propre exception est que si ce n'est pas une erreur de programmation du style une division par 0,
à la différence des instructions 'raise' et 'assert', même s'il y a un message d'erreur, le programme fonctionnera
toujours car on a utilisé les fonctions try / except alors que ce n'est pas une erreur de programmation

Éditeur : Laurent REYNAUD
Date : 10-09-2020
"""


class mon_exception(Exception):
    """ Pour créer sa propre exception, il faut créer une classe avec le nom de sa propre exception qui doît être
    héritée de la classe parente 'Exception' """

    def __init__(self, message):  # Constructeur
        self.message = message

    def __str__(self):  # Message à afficher
        return f'Erreur trouvé : {self.message}'


print('Age : ')
age = int(input())

if age < 18:
    try:
        raise mon_exception('âge non admis')
    except mon_exception as e:
        print(e)
    finally:
        print('Age saisi :', age)
else:
    print('Age saisi :', age)
