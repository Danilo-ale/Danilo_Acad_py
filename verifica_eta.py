
# Descrizione: Scrivi un programma che chieda all'utente la sua età. Se l'età è
# inferiore a 18 anni, il programma dovrebbe stampare "Mi dispiace, non puoi
# vedere questo film". 

# Altrimenti, dovrebbe stampare "Puoi vedere questo film".


lista_eta=["film1", "film2"]
lista_no_eta=["film3", "film4"]
film=input("Inserisci nome film: ")
if film in lista_eta:
    eta=int(input("Inserisci la tua età: "))
    if(eta<18):
        print("Mi dispiace, non puoi vedere questo film")
    else:
        print("buona visione")
elif(film in lista_no_eta):
        print("buona visione")
else:
     print("scelta sbagliata")