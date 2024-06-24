""""
Scrivete una programma che richiede una lista di numeri all'utente
 e fornisce in output un istogramma basato su questi numeri,
usando asterischi per disegnarlo.
Data ad esempio la lista [3, 7, 9, 5], il programma dovrà
produrre questasequenza:
***
*******
*********
*****

"""
contr=True
while contr:
    counter=0
    numeri=input("Inserisci una sequenza di numeri separati da uno spazio: ")
    lista_num=numeri.split(" ")
    print(lista_num)
    for numero in lista_num:
        if not numero.isdecimal():
            print("Vi è un valore non valido")
            counter+=1
    if counter!=0:
        print("Reinsirisci i valori")
    else:
        contr=False

lista_ast=[]
for numero in lista_num:
    print()
    for i in range(int(numero)):
        print("*", end = "")
print()
for numero in lista_num:
    print("*"*int(numero))