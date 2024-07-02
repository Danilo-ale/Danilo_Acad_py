import modulo_classe

while True:
    stringa=input("Inserisci una sequenza di numeri divisi da uno spazio: ")
    v1=modulo_classe.Vendite(stringa)
    if v1.lista=="ERROR":
        print("Reinserisci i valori")
    else:
        #print("Valori lista:", v1.lista)
        break
    
print(v1.calcolo_totale())
print(v1.calcolo_media())
print(v1.vend_sopra_media())
