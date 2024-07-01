def classi():
    # Definizione della classe Scuderia
    class Scuderia:
        numero_di_scuderie = 10  # Attributo di classe

        def __init__(self, nome_scuderia, nomi_piloti):
            # Metodo di inizializzazione dell'oggetto Scuderia
            self.nome_scuderia = nome_scuderia
            self.nomi_piloti = nomi_piloti

        def info(self):
            # Metodo per stampare le informazioni della scuderia
            print(f"Nome Scuderia: {self.nome_scuderia}")
            print("Nomi Piloti:")
            for pilota in self.nomi_piloti:
                print(f"- {pilota}")
        def nomeScuderia(self):
            print(self.nome_scuderia)

    # Lista per memorizzare le scuderie create
    lista_scuderie = []

    # Esempio di utilizzo della classe Scuderia
    scuderia1 = Scuderia("Ferrari", ["Charles Leclerc", "Carlos Sainz"])
    scuderia2 = Scuderia("Mercedes", ["Lewis Hamilton", "George Russell"])

    # Aggiungere le scuderie create alla lista
    lista_scuderie.append(scuderia1)
    lista_scuderie.append(scuderia2)

    # Stampare le informazioni delle scuderie esistenti
    for scuderia in lista_scuderie:
        scuderia.info()

    # Chiedere all'utente se desidera aggiungere una nuova scuderia
    while True:
        risposta = input("Desideri aggiungere un'altra scuderia? (sì/no): ").lower()
        if risposta != 'sì' and risposta != 'si':
            break
        
        # Chiedere il nome della nuova scuderia
        nome_scuderia = input("Inserisci il nome della nuova scuderia: ")

        # Chiedere i nomi dei piloti della nuova scuderia
        nomi_piloti = []
        while True:
            pilota = input("Inserisci il nome del pilota (invia un campo vuoto per terminare): ")
            if pilota == "":
                break
            nomi_piloti.append(pilota)

        # Creare un'istanza della nuova scuderia e aggiungerla alla lista
        nuova_scuderia = Scuderia(nome_scuderia, nomi_piloti)
        lista_scuderie.append(nuova_scuderia)

    # Stampare le informazioni aggiornate di tutte le scuderie
    print("\nElenco aggiornato delle scuderie:")
    for scuderia in lista_scuderie:
        print("Nome scuderia: ",scuderia.nomeScuderia())
        scuderia.info()

def menu():
    # Funzione per mostrare il menu
    print("Ecco un menù di cosa ho imparato")
    print("1. Classi (La funzione si trova a riga 1 del codice)")

    # Chiedere all'utente cosa desidera vedere
    scelta = input("Scegli cosa vedere: ")
    if scelta == "1":
        classi()  # Chiamare la funzione classi() per mostrare l'esempio di classe

# Eseguire la funzione menu() per avviare il programma
menu()
