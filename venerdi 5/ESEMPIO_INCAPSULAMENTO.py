"""
-incapsulamento: nascondere i dettagli implementativi di una classe, in modo da esporre solo ciò che è necessario all'esterno.
I vari metodi per implementare una forma di incapsulamento sono: 1. Utilizzo di attributi privati e protetti.
 I primi vengono scritti  con il nome dell'attributo preceduto da due underscore. Questi non possono essere modificati o visualizzabili all'esterno della classe.
   Gli attributi protetti invece si creano precedendo il nome dell'attributo con un singolo underscore. A differenza dei due underscore 
   utilizzati per gli attributi privati (che rendono di fatto inaccessibile l'attributo dall'esterno), il singolo underscore per gli attributi protetti 
   è una convenzione utilizzata dai programmatori, per segnalare che l'attributo protetto debba essere utilizzato solo ed unicamente all'interno della 
   classe padre e delle classi figlie. 2. Il secondo metodo per l'incapsulamento è l'utilizzo dei metodi "getter" e "setter" che permettono, rispettivamente,
     di ottenere e modificare gli attributi privati di una classe. 
"""

