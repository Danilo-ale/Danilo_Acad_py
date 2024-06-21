"""Scrivi un sistema ché faccia quanto segue:

Chieda all'utente di inserire una stringa.
Conti quante vocali (a, e, i, o, u, sia maiuscole che minuscole) sono presenti nella stringa.
Stampi il numero di vocali trovate nella stringa."""

vocali=["a","e","i","o","u"]                #lista delle vocali
stringa=input("Inserisci una stringa: ")       
cont=0              #contatore vocali  #per ogni vocale nella lista cerca se è presente nella stringa
         
for i in stringa:
    if(i in vocali):
        cont+=1      

print("Numeri vocali: ", cont)          #stampa contatore