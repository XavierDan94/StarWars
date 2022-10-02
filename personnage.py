class Personnage:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def __str__(self):
        return "*** Description d'un personnage *** \n" + "Nom : " + self.get_nom() + "\nPrénom : " + self.get_prenom()
