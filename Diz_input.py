#richieste input
booll=input("True o False? ")
int=input("Scrivi un intero: ")
stringa=input("Scrivi una stringa: ")
print(booll,int,stringa)

#inserimento in lista
lista=[booll,int,stringa]
print(lista)

#inserimento in dizionario
dizionario={
    "tipididato": lista
}
print(dizionario)
print(dizionario.keys())
print(dizionario.get("tipididato"))
