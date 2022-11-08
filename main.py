# Questo è un commento

class Persona:
    def __init__(self, nome, cognome) -> None:
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("ciao sono " + self.nome + " " + self.cognome)

class Insegnante(Persona):  #Insegnante estende Persona
    def __init__(self, nome, cognome, materia) -> None:
        super().__init__(nome, cognome)
        self.materia = materia

    def saluta(self):
        print("Buongiorno sono {0} {1} ed insegno {2}".format(self.nome, self.cognome, self.materia))

# persona1 = Persona(nome="Luca", cognome="Piccinelli")
# persona1.saluta()

Insegnante1 = Insegnante(nome="Mario", cognome="Rossi", materia="lettere")
Insegnante1.saluta()

import mymodule as mm
mm.saluta("Luca")

import platform
print(platform.system() + " " + platform.version())

import datetime

x = datetime.datetime.now()
print(x.strftime("%d/%m/%Y"))