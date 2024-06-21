"""Scrivi un sistema ché faccia quanto segue:

Chieda all'utente di inserire una stringa.
Conti quante vocali (a, e, i, o, u, sia maiuscole che minuscole) sono presenti nella stringa.
Stampi il numero di vocali trovate nella stringa."""

vocali=["a","e","i","o","u"]                #lista delle vocali
stringa=input("Inserisci una stringa: ").lower()
cont=0              #contatore vocali  
         
for i in stringa:           #per ogni lettera controlla se è presente nella lista vocali 
    if(i in vocali):
        cont+=1                 #se è presente, aumenta il contatore      

print("Numeri vocali: ", cont)          #stampa contatore