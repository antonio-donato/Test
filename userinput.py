Persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}

operazioni = ("aggiungi", "aggiorna", "cancella")

def start():
    operazione = input("cosa vuoi fare? ")
    if operazione == operazioni[0]:
        x = input("Aggiungi chiave valore separati da una virgola: ")
        aggiungi(x.split(","))
    elif operazione == operazioni[1]:
        chiavi = Persona.keys
        print(type(chiavi))
        x = input("Quale chiave vuo aggiornare tra le seguenti: {0}/{1}/{2}".format(chiavi[0], chiavi[1], chiavi[2]))
    elif operazione == operazioni[2]:
        pass

def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    Persona[chiave] = valore
    print(Persona)

def aggiorna(param):
    chiave = param[0]
    valore = param[1]
    Persona[chiave] = valore
    print(Persona)

while True:
    start()
