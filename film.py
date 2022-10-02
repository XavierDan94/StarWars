class Film:
    # Constructeur de la classe Film
    def __init__(self, titre, sortie, episode, cout, recette, acteurs=None, personnages=None):
        """
        Constrcuteur de la classe film
        :param titre: (str)
        :param sortie: (int)
        :param episode: (str)
        :param cout: (int)
        :param recette: (int)
        :param acteurs: (Acteur)
        :param personnages: (Personnage)
        """
        self.titre = titre
        self.sortie = sortie
        self.episode = episode
        self.cout = cout
        self.recette = recette
        if acteurs is None:
            self.acteurs = []
        self.acteurs = acteurs
        if personnages is None:
            self.personnages = []
        self.personnages = personnages

    # Getters
    def get_titre(self):
        """Permet d'obtenir le titre d'un film"""
        return self.titre

    def get_sortie(self):
        """
        Permet d'obtenir l'année de sortir d'un film
        :return:
        """
        return self.sortie

    def get_episode(self):
        """
        Permet d'obtenir le titre d'un épisode
        :return:
        """
        return self.episode

    def get_cout(self):
        """
        Permet d'obtenir le coût d'un film
        :return:
        """
        return self.cout

    def get_recette(self):
        """
        Permet d'obtenir la recette d'un film
        :return:
        """
        return self.recette

    def get_acteurs(self):
        """
        Permet d'obtenir la liste des acteurs
        :return:
        """
        liste = ""
        for i in range(0, len(self.acteurs)):
            liste += str(self.acteurs[i]) + " / "
        return liste

    # Setters
    def set_titre(self, titre):
        """
        Permet de définir le titre du film
        :param titre: (str)
        :return:
        """
        self.titre = titre

    def set_sortie(self, sortie):
        """
        Permet de définir l'année de sortie
        :param sortie: (str)
        :return:
        """
        self.sortie = sortie

    def set_episode(self, episode):
        """
        Permet de définir le titre de l'épisode
        :param episode: (str)
        :return:
        """
        self.episode = episode

    def set_cout(self, cout):
        """
        Permet de définir le coût d'un film défini
        :param cout: (int)
        :return:
        """
        self.cout = cout

    def set_recette(self, recette):
        """
        Permet de définir la recette générée pour un film
        :param recette: (int)
        :return:
        """
        self.recette = recette

    def set_acteurs(self, acteur):
        """
        Permet d'ajouter un acteur dans une liste
        :param acteur: (Acteur)
        :return:
        """
        for i in range(0, len(acteur)):
            if i == 0:
                self.acteurs = [acteur[i]]
            else:
                self.acteurs += ([acteur[i]])

    # Redéfinition de la méthode __str__
    def __str__(self):
        acteurs = self.get_acteurs()
        return "Titre : " + self.get_titre() + "\nAnnée de sortie: " + str(self.get_sortie()) + "\nNuméro d'épisode: " \
               + self.get_episode() + "\nCoût: " + str(self.get_cout()) + " EUR\nRecette: " + str(self.get_recette()) +\
               " EUR\nActeurs: " + acteurs

    def nb_acteurs(self):
        """
        Retourne le nombre d'acteurs présents dans un film donné
        :return:
        """
        return 0 if self.acteurs is None else len(self.acteurs)

    def nb_personnages(self):
        """
        Retourne le nombre de personnages d'un film
        :return:
        """
        return 0 if self.personnages is None else len(self.personnages)

    def calcul_benefice(self):
        """
        Permet de savoir si le film est bénéficiaire et calcule le bénéfice
        :return:
        """
        est_beneficiaire = False
        resultat = self.get_recette() - self.get_cout()
        if self.get_recette() > self.get_cout():
            est_beneficiaire = True
        return resultat, est_beneficiaire

    def is_before(self, annee):
        """
        Permet de savoir si le film est sorti avant une année passée en paramètre
        :param annee: (int)
        :return:
        """
        return True if self.get_sortie() < annee else False
