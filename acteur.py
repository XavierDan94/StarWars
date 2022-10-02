class Acteur:
    def __init__(self, nom, prenom, personnages=None):
        self.nom = nom
        self.prenom = prenom
        if personnages is None:
            self.personnages = []
        self.personnages = personnages

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_personnage(self):
        liste = ""
        for i in range(0, len(self.personnages)):
            liste += str(self.personnages[i]) + " / "
        return liste

    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_personnage(self, personnage):
        for i in range(0, len(personnage)):
            if i == 0:
                self.personnages = [personnage[i]]
            else:
                self.personnages += ([personnage[i]])

    def __str__(self):
        return self.get_prenom() + " " + self.get_nom()

    def nb_personnages(self):
        return len(self.personnages)
