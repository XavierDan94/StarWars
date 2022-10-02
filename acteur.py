class Acteur:
    def __init__(self, nom, prenom, personnages=None):
        """
        :param nom:
        :param prenom:
        :param personnages:
        Constructeur de la classe Acteur
        """
        self.nom = nom
        self.prenom = prenom
        if personnages is None:
            self.personnages = []
        self.personnages = personnages

    def get_nom(self):
        """
        Permet d'obtenir le nom d'un acteur
        :return: self.nom (str)
        """
        return self.nom

    def get_prenom(self):
        """
        Permet d'obtenir le prénom d'un acteur
        :return: self.prenom (str)
        """
        return self.prenom

    def get_personnage(self):
        """
        Permet d'obtenir une liste de personnages joués par un acteur
        :return: liste
        """
        liste = ""
        for i in range(0, len(self.personnages)):
            liste += str(self.personnages[i]) + " / "
        return liste

    def set_nom(self, nom):
        """
        Permet de définir le nom d'un acteur
        :param nom:
        :return:
        """
        self.nom = nom

    def set_prenom(self, prenom):
        """
        Permet de définir le prénom d'un acteur
        :param prenom:
        :return:
        """
        self.prenom = prenom

    def set_personnage(self, personnage):
        """
        Permet de définir un ou plusieurs personnages joués par un acteur
        :param personnage:
        :return:
        """
        for i in range(0, len(personnage)):
            if i == 0:
                self.personnages = [personnage[i]]
            else:
                self.personnages += ([personnage[i]])

    def __str__(self):
        return self.get_prenom() + " " + self.get_nom()

    def nb_personnages(self):
        """
        Permet d'obtenir le nombre de personnages joués par un acteur
        :return: len(self.personnages) (int)
        """
        return len(self.personnages)
