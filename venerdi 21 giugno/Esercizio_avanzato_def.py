#sequenza di Fibonacci
def Fibonacci(max):
    a=1         #fn-2
    b=1         #fn-1
    sum=0
    print(a)        #stampa per visualizzare la seq. di Fibonacci
    print(b)
    controllo=0
    while True:      #ripete fino a quando sum<max
        controllo=sum   #variabile di comodo
        sum=a+b         #sommo fn=fn-1 + fn-2
        a=b
        b=sum
        
        if sum>max:     #se sum diventa > max
            print("Numero che sfora il max: ",sum)
            break   #termina il break
        else:
            print(sum)
    return controllo        #e ritorna la variabile controllo, che ha il valore precedente di somma (che è diventato maggiore di max)



max=int(input("Inserisci il numero massimo della sequenza: "))  #input max
somma=Fibonacci(max)        #richiamo funzione
print("\n\nLa somma di Fibonacci fino al numero inserito è: ",somma)