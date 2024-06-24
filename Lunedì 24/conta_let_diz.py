"""
Scrivete un programma che chiede una stringa 
all'utente e restituisce un dizionario rappresentante
 la "frequenza di comparsa" di ciascun carattere 
 componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}
"""
dizionario={}

stringa=input("Inserisci stringa: ").lower()
lista_let=[]
lista_cont=[]

for let in stringa:
    cont=stringa.count(let)
    print("Conteggio di",let,":", cont)
    if let not in lista_let and let!=" ":
        lista_let.append(let)
        lista_cont.append(cont)
for let in lista_let:
    dizionario.update({let : lista_cont[lista_let.index(let)]})



for let in lista_let:
    print(f"Lettera {let} ripetuta {lista_cont[lista_let.index(let)]} volte") 


print(dizionario)
