import parteuno as mod1     #import modulo con funzioni

#menu
def menu():
    print("""\nMenù:
1. Stampa matrice
2. Estrai sottomatrice
3. Matrice trasposta        
4. Somma elementi matrice
5. Moltiplicazione element-wise
6. Media elementi matrice
7. Calcolo determinante                     
0. Esci
""")
    scelta_menu=input("\nScegli un opzione: ")
    return scelta_menu

#main
def main():
    print("\nCreazione Matrice 2D...\n")
    mat,righe,col=mod1.crea_matrice()   #creazione della matrice di partenza fuori dal while

    while True:
        scelta=menu()
        if scelta=="1":         #Stampa matrice
            print(f"\nLa matrice 2D di partenza è:\n {mat}")
        elif scelta=="2":       #Estrai sottomatrice
            mod1.sotto_matrice(mat,righe,col)
        elif scelta=="3":       #Matrice trasposta
            mod1.trasp_matrice(mat)
        elif scelta=="4":       #Somma elementi matrice
            mod1.somma_elem(mat)
        elif scelta=="5":       #Moltiplicazione element-wise
            mod1.molt_elem_wise(mat,righe,col)
        elif scelta=="6":       #Media elementi matrice
            mod1.media_mat(mat)
        elif scelta=="7":       #Calcolo determinante
            mod1.det_mat(mat,righe,col)
        elif scelta=="0":       #Esci
            break
        else:
            print("Scelta sbagliata")

        nuova_scelta = input("\nVuoi effettuare un'altra operazione? ") #ripetibilità gestita tramite la richiesta di una nuova operazione
        if nuova_scelta.lower() != "si":
            print("\nSistema in chiusura. Arrivederci!")
            break


main()      #richiamo al main