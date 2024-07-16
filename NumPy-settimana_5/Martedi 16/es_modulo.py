import parteuno as mod1

def menu():
    print("""1. Stampa matrice
2. Estrai sottomatrice
3. Matrice trasposta        
4. Somma elementi matrice
5. Moltiplicazione element-wise
6. Media elementi matrice
7. Calcolo determinante                     
0. Esci
""")
    scelta_menu=input("Inserisci una scelta: ")
    return scelta_menu

def main():
    mat,righe,col=mod1.crea_matrice()
    while True:
        scelta=menu()
        if scelta=="1":
            print(f"La matrice è:\n {mat}")
        elif scelta=="2":
            mod1.sotto_matrice(mat,righe,col)
        elif scelta=="3":
            mod1.trasp_matrice(mat)
        elif scelta=="4":
            mod1.somma_elem(mat)
        elif scelta=="5":
            mod1.molt_elem_wise(mat,righe,col)
        elif scelta=="6":
            mod1.media_mat(mat)
        elif scelta=="7":
            mod1.det_mat(mat,righe,col)
        elif scelta=="0":
            break
        else:
            print("Scelta sbagliata")

main()