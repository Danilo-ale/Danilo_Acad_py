class Animale:
    def __init__(self, nome, età):
        self.nome=nome
        self.età=età
    
    
    def fai_suono(self, suono):
        print(suono)

class Leone(Animale):
    def __init__(self, nome, età):
        super().__init__(nome, età)
    """def __init__(self, nome, età):
        Animale.__init__(self,nome, età)"""

    def fai_suono(self):
        print("Sono il leone: roar")
    
    def caccia(self):
        print("Ogni mattina, in Africa, appena sorge il sole...")

class Giraffa(Animale):
    def __init__(self, nome, età):
        super().__init__(nome, età)
    
    def getEta(self):
        return self.età
    
    def fai_suono(self):
        print("Sono la giraffa: gir")


an1=Animale("Pippo",5)
an2=Leone("Leoone", 10)
an2.fai_suono()
an2.caccia()
an3=Giraffa("Giri", 20)
print(an3.getEta())