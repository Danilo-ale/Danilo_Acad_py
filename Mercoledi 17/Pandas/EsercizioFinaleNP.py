"""---Partecipanti Gruppo: Daniele Danilo Matteo---"""

import ModuloEsercizioFinaleNP as mod1     #import modulo con funzioni


def menu(): #menu
    print("""\nMenù:
1. Stampa matrice
2. Estrai sottomatrice
3. Matrice trasposta        
4. Somma elementi matrice
5. Moltiplicazione element-wise
6. Media elementi matrice
7. Calcolo determinante  
8. Calcolo matrice inversa
9. Filtra elementi matrice 
10.Funzioni matematiche (Seno,Coseno, Esponenziale)                
0. Esci
""")
    scelta_menu=input("\nScegli un opzione: ")
    return scelta_menu

def main(): #main
    print("\nCreazione Matrice 2D...\n")
    mat,righe,col=mod1.crea_matrice()   #creazione della matrice di partenza fuori dal while

    while True:
        scelta=menu()
        if scelta=="1":         #Stampa matrice
            print(f"\nLa matrice 2D di partenza è:\n {mat}")
        elif scelta=="2":       #Estrai sottomatrice
            if mod1.scelta():
                mat1,righe1,col1 = mod1.crea_matrice()
                mod1.sotto_matrice(mat1,righe1,col1)
            else:
                mod1.sotto_matrice(mat,righe,col)
        elif scelta=="3":       #Matrice trasposta
            if mod1.scelta():
                mat1,righe1,col1 = mod1.crea_matrice()
                mod1.trasp_matrice(mat1)
            else:
                mod1.trasp_matrice(mat)
        elif scelta=="4":       #Somma elementi matrice
            if mod1.scelta():
                mat1,righe1,col1 = mod1.crea_matrice()
                mod1.somma_elem(mat1)
            else:
                mod1.somma_elem(mat)
        elif scelta=="5":       #Moltiplicazione element-wise
            if mod1.scelta():
                mat1,righe1,col1 = mod1.crea_matrice()
                mod1.molt_elem_wise(mat1,righe1,col1)
            else:
                mod1.molt_elem_wise(mat,righe,col)
        elif scelta=="6":       #Media elementi matrice
            if mod1.scelta():
                mat1,righe1,col1 = mod1.crea_matrice()
                mod1.media_mat(mat1)
            else:
                mod1.media_mat(mat)
        elif scelta=="7":       #Calcolo determinante
            if mod1.scelta():
                mat1,righe1,col1 = mod1.crea_matrice()
                mod1.det_mat(mat1,righe1,col1)
            else:
                mod1.det_mat(mat,righe,col)
        elif scelta=="8":
            if mod1.scelta():
                mat1,righe1,col1 = mod1.crea_matrice()
                mod1.matrice_inversa(mat1,righe1,col1)
            else:
                mod1.matrice_inversa(mat,righe,col)
        elif scelta=="9":
            if mod1.scelta():
                mat1,righe1,col1 = mod1.crea_matrice()
                mod1.filtro_mat(mat1)
            else:
                mod1.filtro_mat(mat)
        elif scelta=="10":
            if mod1.scelta():
                mat1,righe1,col1 = mod1.crea_matrice()
                mod1.funzione_matematica(mat1)
            else:
                mod1.funzione_matematica(mat)
        elif scelta=="0":       #Esci
            break
        else:
            print("Scelta sbagliata")

        nuova_scelta = input("\nVuoi effettuare un'altra operazione? ") #ripetibilità gestita tramite la richiesta di una nuova operazione
        if nuova_scelta.lower() != "si":
            print("\nSistema in chiusura. Arrivederci!")
            break

main()      #richiamo al main