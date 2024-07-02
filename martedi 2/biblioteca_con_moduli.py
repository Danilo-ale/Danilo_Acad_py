import mod_Libreria     #importazione file mod_Libreria.py


lb1=mod_Libreria.Libreria("Libreriona")     #creazione oggetto libreria
print(f"Benvenuto nella libreria {lb1.getNome()}")

#MENU
def menu():
    print("""\n1. Aggiungi libro
2. Rimuovi libro
3. Cerca libri per titolo
4. Visualizza catalogo
0. Esci
""")
    

while True:     #CICLO WHILE
    menu()
    scelta=input("Seleziona un'opzione: ")
    if scelta=="1":     #Aggiungi libro
        lb1.aggiungi_libro()
    elif scelta=="2":       #Rimuovi libro
        isbn_r=input("Inserisci l'isbn del libro da rimuovere: ")
        lb1.rimuovi_libro(isbn_r)
    elif scelta=="3":       #Cerca libri per titolo
        titolo=input("Inserisci il titolo del libro che vuoi cercare: ")
        lb1.cerca_per_titolo(titolo)
    elif scelta=="4":   #Visualizza catalogo
        lb1.mostra_catalogo()
    elif scelta=="0":       #esci
        break
    else:
        print("Scelta sbagliata")


print("CHIUSURA PROGRAMMA")